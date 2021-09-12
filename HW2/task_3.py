import yaml


data = {
    'key1': [1, 2, 'a'],
    'key2': 12345,
    'key3': {
        1: 'Э',
        2: 'Ё',
    }
}

with open('file.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f:
    f_content = yaml.load(f)

print(f_content)
