import itertools

DELETED = "- "
ADDED = "+ "
EMPTY = "  "
REPLACER = "  "


def to_str(data):
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return 'null'
    return data


def style_maker(dict_diff):
    def iter_(data, depth, spaces_count=1):

        if not isinstance(data, dict):
            return str(data)

        depth_size = depth + spaces_count
        deep_indent = REPLACER * depth_size
        current_indent = REPLACER * depth
        lines = []

        for k, v in sorted(data.items()):
            if isinstance(v, dict) and "action" in v:
                method = v.get('action')

                if method == 'record added':
                    lines.append(
                        f"{deep_indent}{ADDED}{k}: "
                        f"{iter_(to_str(v.get('value')), depth_size + 1)}"
                    )
                if method == 'record deleted':
                    lines.append(
                        f"{deep_indent}{DELETED}{k}: "
                        f"{iter_(to_str(v.get('value')), depth_size + 1)}"
                    )
                if method == 'record changed':
                    lines.append(
                        f"{deep_indent}{DELETED}{k}: "
                        f"{iter_(to_str(v.get('previous')), depth_size + 1)}"
                    )
                    lines.append(
                        f"{deep_indent}{ADDED}{k}: "
                        f"{iter_(to_str(v.get('current')), depth_size + 1)}"
                    )
                if method == 'record nested':
                    lines.append(
                        f"{deep_indent}{EMPTY}{k}: "
                        f"{iter_(to_str(v.get('children')), depth_size + 1)}"
                    )
                if method == 'record is the same':
                    lines.append(
                        f"{deep_indent}{EMPTY}{k}: "
                        f"{iter_(to_str(v.get('value')), depth_size + 1)}"
                    )
            else:
                lines.append(
                    f"{deep_indent}{EMPTY}{k}: "
                    f"{iter_(to_str(v), depth_size + 1)}"
                )
        result1 = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result1)

    result = iter_(dict_diff, 0)
    return result
