import json

def generate_diff(file1, file2):

    source1 = json.load(open(file1))
    source2 = json.load(open(file2))

    all_keys = set(list(source1.keys()) + list(source2.keys()))
    diff = ""

    for i in sorted(all_keys):
        if i in source1 and i in source2:
            if source1[i] == source2[i]:
                diff += f'{i}: {source1[i]}\n'
            else:
                diff += f'-{i}: {source1[i]}\n+{i}: {source2[i]}\n'
        elif i in source1 and i not in source2:
            diff += f'-{i}: {source1[i]}\n'
        elif i not in source1 and i in source2:
            diff += f'+{i}: {source2[i]}\n'

    return f'{{\n{diff}}}'
