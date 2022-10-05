import json
import yaml


def parse(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ('yml', 'yaml'):
        return yaml.safe_load(content)
    raise Exception(f"Unknown format: {format}")
