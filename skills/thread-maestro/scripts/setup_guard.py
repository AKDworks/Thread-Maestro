"""Track one task's agreed setup revision and creation attempts. Standard library only.

This checks consistency, not user authorization or actual Codex project membership.
Keep its state in a task-owned location outside the product being organized.
"""
import argparse
import json
import ntpath
import os
from pathlib import Path


def clean_path(value):
    value = value.strip()
    if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1].strip()
    if any(ord(char) < 32 for char in value):
        raise ValueError('A path cannot contain control characters.')
    if ntpath.isabs(value) and (ntpath.splitdrive(value)[0] or value.startswith('\\\\')):
        return ntpath.normcase(ntpath.normpath(value))
    if value.startswith('/'):
        return os.path.normpath(value)
    raise ValueError('An absolute folder path is required.')


def canonical(data):
    result = {key: data[key] for key in (
        'planId', 'projectName', 'totalChats', 'newChats', 'chatNames',
        'chatRoles', 'files', 'firstReplyMode')}
    total = result['totalChats']
    if type(total) is not int or total not in (3, 5, 7):
        raise ValueError('Supported totals: 3, 5, 7.')
    for field in ('planId', 'projectName'):
        if not isinstance(result[field], str) or not result[field].strip():
            raise ValueError(f'Invalid {field}.')
    for field in ('chatNames', 'chatRoles'):
        values = result[field]
        if not isinstance(values, list) or len(values) != total or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError(f'{field} must describe every chat.')
    if len(set(result['chatNames'])) != total:
        raise ValueError('Chat names must be distinct.')
    result['reusedChats'] = data.get('reusedChats', {})
    if not isinstance(result['reusedChats'], dict) or any(name not in result['chatNames'] or not isinstance(identifier, str) or not identifier for name, identifier in result['reusedChats'].items()):
        raise ValueError('Reused chats require known names and real IDs.')
    if type(result['newChats']) is not int or result['newChats'] != total - len(result['reusedChats']):
        raise ValueError('New and reused counts must match the structure.')
    if result['firstReplyMode'] not in ('acknowledgment', 'inactive', 'manual'):
        raise ValueError('Choose a concrete startup mode.')
    if not isinstance(result['files'], list) or any(not isinstance(v, str) or not v or ntpath.isabs(v) or ntpath.splitdrive(v)[0] or '..' in v.replace('\\', '/').split('/') for v in result['files']):
        raise ValueError('Planned files must remain relative to the project.')
    result['chatDependencies'] = data.get('chatDependencies', [])
    if not isinstance(result['chatDependencies'], list) or any(not isinstance(v, str) for v in result['chatDependencies']):
        raise ValueError('Dependencies must be a list of plain text descriptions.')
    return result


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def run(state, args):
    if args.action == 'register':
        plan = canonical(read_json(args.input))
        current = state.get('plan')
        if current and current['planId'] == plan['planId']:
            if current != plan:
                raise ValueError('A changed plan requires a new planId and confirmation.')
        else:
            old_steps = state.get('runs', {}).get(current['planId'], {}).get('steps', {}) if current else {}
            if any(step['status'] not in ('ready', 'failed') for step in old_steps.values()):
                raise ValueError('Resolve earlier creation attempts before replacing their plan.')
            if plan['planId'] in state.setdefault('revisions', []):
                raise ValueError('A retired planId cannot become current again.')
            state['plan'] = plan
            state['revisions'].append(plan['planId'])
        return {'planId': plan['planId'], 'registered': True}
    plan = state.get('plan')
    if not plan:
        raise ValueError('Register the displayed plan first.')
    if args.plan_id != plan['planId']:
        raise ValueError('Stale planId: continue only the current setup revision.')
    if args.action == 'begin':
        confirmation = read_json(args.input)
        if canonical(confirmation) != plan:
            raise ValueError('Stale or changed confirmation: use the latest displayed plan.')
        folder = clean_path(confirmation['folder'])
        project = confirmation['projectId']
        if not isinstance(project, str) or not project:
            raise ValueError('Use the project ID verified through the app tools.')
        runs = state.setdefault('runs', {})
        existing = runs.get(plan['planId'])
        if existing and (existing['folder'] != folder or existing['projectId'] != project):
            raise ValueError('A different target requires a new setup revision.')
        if not existing:
            runs[plan['planId']] = {'folder': folder, 'projectId': project, 'steps': {}}
        return report(state)
    current_run = state.get('runs', {}).get(plan['planId'])
    if not current_run:
        raise ValueError('Validate the human-confirmed setup with begin first.')
    if args.action == 'status':
        return report(state)
    if plan['firstReplyMode'] == 'manual':
        raise ValueError('Manual mode does not authorize automatic chat creation.')
    name = args.chat
    if name not in plan['chatNames'] or name in plan['reusedChats']:
        raise ValueError('This is not a planned missing chat.')
    steps = current_run['steps']
    previous = steps.get(name, {})
    if args.action == 'claim':
        if previous.get('status') not in (None, 'failed'):
            return {'create': False, 'chat': name, **previous}
        steps[name] = {'status': 'in_flight'}
        return {'create': True, 'chat': name}
    status = args.status
    if not previous:
        raise ValueError('Claim a creation before recording its result.')
    if previous.get('status') == 'ready' and status != 'ready':
        raise ValueError('Do not downgrade a verified ready chat.')
    if status in ('created', 'ready') and not args.thread_id:
        raise ValueError('A real thread ID is required.')
    if status == 'preparing' and not args.client_thread_id:
        raise ValueError('Record the returned temporary ID.')
    if status == 'failed' and (previous.get('threadId') or previous.get('clientThreadId')):
        raise ValueError('A returned ID must be checked, not blindly retried.')
    record = {**previous, 'status': status}
    for key, value in (('threadId', args.thread_id), ('clientThreadId', args.client_thread_id), ('hostId', args.host)):
        if value:
            record[key] = value
    if previous.get('threadId') and args.thread_id and previous['threadId'] != args.thread_id:
        raise ValueError('Conflicting thread IDs require investigation.')
    steps[name] = record
    return report(state)


def report(state):
    plan = state['plan']
    current_run = state.get('runs', {}).get(plan['planId'], {})
    steps = current_run.get('steps', {})
    pending = [name for name in plan['chatNames'] if name not in plan['reusedChats'] and steps.get(name, {}).get('status') in (None, 'failed')]
    unresolved = [name for name, step in steps.items() if step['status'] not in ('ready', 'failed')]
    ready = sum(step['status'] == 'ready' for step in steps.values())
    return {'planId': plan['planId'], 'pending': pending, 'unresolved': unresolved,
            'ready': ready, 'reused': len(plan['reusedChats']), 'steps': steps,
            'complete': plan['firstReplyMode'] != 'manual' and ready == plan['newChats']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--state', required=True)
    parser.add_argument('--plan-id')
    actions = parser.add_subparsers(dest='action', required=True)
    for action in ('register', 'begin'):
        command = actions.add_parser(action)
        command.add_argument('input')
    for action in ('claim', 'record'):
        command = actions.add_parser(action)
        command.add_argument('chat')
        if action == 'record':
            command.add_argument('--status', required=True, choices=('created', 'preparing', 'ready', 'failed', 'outcome_unknown'))
            command.add_argument('--thread-id')
            command.add_argument('--client-thread-id')
            command.add_argument('--host')
    actions.add_parser('status')
    args = parser.parse_args()
    location = Path(args.state).resolve()
    location.parent.mkdir(parents=True, exist_ok=True)
    lock = location.with_suffix(location.suffix + '.lock')
    acquired = False
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        acquired = True
        os.close(descriptor)
        state = read_json(location) if location.exists() else {}
        result = run(state, args)
        temporary = location.with_suffix(location.suffix + '.tmp')
        temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
        os.replace(temporary, location)
        print(json.dumps(result, ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(json.dumps({'error': str(error)}, ensure_ascii=False))
        raise SystemExit(1)
    finally:
        if acquired:
            lock.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
