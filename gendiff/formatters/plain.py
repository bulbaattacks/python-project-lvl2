def to_string(data):
    if isinstance(data, bool):
        return str(data).lower()
    if data is None:
        return "null"
    if isinstance(data, dict):
        return "[complex value]"
    return f"'{data}'"


def string_maker(data, path=''):
    lines = []
    for k, v in sorted(data.items()):
        if isinstance(v, dict) and "action" in v:
            method = v.get("action")

            if method == "record added":
                lines.append(
                    f"Property '{path + k}' was added with value:"
                    f" {to_string(v.get('value'))}"
                )
            elif method == "record deleted":
                lines.append(
                    f"Property '{path + k}' was removed"
                )
            elif method == "record changed":
                lines.append(
                    f"Property '{path + k}' was updated."
                    f" From {to_string(v.get('previous'))}"
                    f" to {to_string(v.get('current'))}"
                )
            elif method == "record nested":
                new_path = f"{path}{k}."
                lines.append(
                    string_maker(v.get('children'), new_path)
                )
    return "\n".join(lines)


def format_plain(diff_dict):
    return string_maker(diff_dict)
