import itertools

METHOD_PREFIX = {
    "record added": "+ ",
    "record deleted": "- ",
    "record is the same": "  "
}


def to_str(data):
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return "null"
    return data


def walk(data, depth=0, replacer="  ", spaces_count=1):

    if not isinstance(data, dict):
        return str(data)

    depth_size = depth + spaces_count
    deep_indent = replacer * depth_size
    current_indent = replacer * depth
    lines = []

    for k, v in sorted(data.items()):
        if isinstance(v, dict) and "action" in v:
            method = v.get("action")

            if method == "record changed":
                lines.append(
                    f"{deep_indent}{METHOD_PREFIX['record deleted']}{k}: "
                    f"{walk(to_str(v.get('previous')), depth_size + 1)}"
                )
                lines.append(
                    f"{deep_indent}{METHOD_PREFIX['record added']}{k}: "
                    f"{walk(to_str(v.get('current')), depth_size + 1)}"
                )
            elif method == "record nested":
                lines.append(
                    f"{deep_indent}{METHOD_PREFIX['record is the same']}{k}: "
                    f"{walk(to_str(v.get('children')), depth_size + 1)}"
                )
            else:
                lines.append(
                    f"{deep_indent}{METHOD_PREFIX[v.get('action')]}{k}: "
                    f"{walk(to_str(v.get('value')), depth_size + 1)}"
                )
        else:
            lines.append(
                f"{deep_indent}{METHOD_PREFIX['record is the same']}{k}: "
                f"{walk(to_str(v), depth_size + 1)}"
            )
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def format_stylish(diff_dict):
    return walk(diff_dict)
