from gendiff.parser import parser_content


def get_content(path):
    with open(path, 'r') as file_content:
        return parser_content(file_content.read(), path.split('.')[-1])


def generate_diff(file1, file2):
    source1 = get_content(file1)
    source2 = get_content(file2)

    all_keys = set(list(source1.keys()) + list(source2.keys()))
    diff = ""

    for i in sorted(all_keys):
        if i in source1 and i in source2:
            if source1[i] == source2[i]:
                diff += f'{i}: {source1[i]}\n'
            else:
                diff += f'- {i}: {source1[i]}\n+ {i}: {source2[i]}\n'
        elif i in source1 and i not in source2:
            diff += f'- {i}: {source1[i]}\n'
        elif i not in source1 and i in source2:
            diff += f'+ {i}: {source2[i]}\n'

    return f'{{\n{diff}}}'
