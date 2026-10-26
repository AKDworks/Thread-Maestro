"""Fill the bundled proposal cards; does not create chats or invoke the host."""
import argparse
import json
from pathlib import Path
import re
import uuid


def render(plan, root_id):
    if not isinstance(plan, dict):
        raise ValueError('The plan must be a JSON object.')
    if not re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_-]*', root_id):
        raise ValueError('Use a safe unique root identifier.')
    variants = plan.get('variants')
    if not isinstance(variants, dict) or not variants or any(key not in ('3', '5', '7') for key in variants):
        raise ValueError('Supported proposal totals: 3, 5, 7.')
    if type(plan.get('selected')) is not int or str(plan['selected']) not in variants:
        raise ValueError('The selected total must have a layout.')
    for field in ('countLabel', 'groupLabel'):
        if not isinstance(plan.get(field), str) or not plan[field].strip():
            raise ValueError(f'A localized {field} is required.')
    for total, variant in variants.items():
        if not isinstance(variant, dict):
            raise ValueError('Each layout must be a JSON object.')
        specialists = variant.get('specialists')
        if not isinstance(specialists, list) or len(specialists) != int(total) - 1:
            raise ValueError('The specialist count must match the total minus one.')
        for card in [variant.get('main'), *specialists]:
            if not isinstance(card, dict) or any(not isinstance(card.get(field), str) or not card[field].strip() for field in ('title', 'description')):
                raise ValueError('Each card needs a plain text title and description.')
            if 'icon' in card and (not isinstance(card['icon'], str) or not re.fullmatch(r'[a-z0-9-]+', card['icon'])):
                raise ValueError('Use a Lucide icon name, not markup.')
    template = (Path(__file__).resolve().parent.parent / 'assets' / 'proposal.html').read_text(encoding='utf-8-sig')
    data = json.dumps(plan, ensure_ascii=True).replace('<', '\\u003c')
    return template.replace('{{ROOT_ID}}', root_id).replace('{{PLAN_JSON}}', data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--root-id')
    args = parser.parse_args()
    try:
        destination = Path(args.output)
        if not destination.is_absolute() or destination.suffix.lower() != '.html':
            raise ValueError('Choose an allowed absolute HTML output path.')
        plan = json.loads(Path(args.plan).read_text(encoding='utf-8-sig'))
        fragment = render(plan, args.root_id or f'tm-proposal-{uuid.uuid4().hex}')
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('x', encoding='utf-8', newline='\n') as output:
            output.write(fragment)
        path = destination.resolve().as_posix()
        print(json.dumps({'path': path, 'reference': '\ue200visualize\ue202' + json.dumps({'path': path}, ensure_ascii=False) + '\ue201'}, ensure_ascii=False))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
