import itertools

PREFIX = {
    "record added": "  + ",
    "record deleted": "  - ",
    "record is the same": "    "
}
INTEND = "    "


def to_str(data, space_count=2):
    if data is None:
        return "null"
    if isinstance(data, str):
        return data
    if not isinstance(data, dict):
        return str(data).lower()
    result = "{\n"

    for k, v in data.items():
        result += (
            f"{INTEND * space_count}{k}: "
            f"{to_str(v, space_count + 1)}\n"
        )
    result += INTEND * (space_count - 1) + "}"

    return result


def walk(data, depth=0):

    current_indent = INTEND * depth
    lines = []

    for k, v in sorted(data.items()):
        if isinstance(v, dict) and "action" in v:
            method = v.get("action")

            if method == "record changed":
                lines.append(
                    f"{INTEND * depth}{PREFIX['record deleted']}{k}: "
                    f"{to_str(v.get('previous'), depth + 2)}"
                )
                lines.append(
                    f"{INTEND * depth}{PREFIX['record added']}{k}: "
                    f"{to_str(v.get('current'), depth + 2)}"
                )
            elif method == "record nested":
                lines.append(
                    f"{INTEND * depth}{PREFIX['record is the same']}{k}: "
                    f"{walk(v.get('children'), depth + 1)}"
                )
            else:
                lines.append(
                    f"{INTEND * depth}{PREFIX[v.get('action')]}{k}: "
                    f"{to_str(v.get('value'), depth + 2)}"
                )
        else:
            lines.append(
                f"{INTEND * depth}{PREFIX['record is the same']}{k}: "
                f"{to_str(v, depth + 2)}"
            )
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def format_stylish(diff_dict):
    return walk(diff_dict)
