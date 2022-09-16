import json
import yaml


def parser_content(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ('yml', 'yaml'):
        return yaml.safe_load(content)
    raise Exception(f"Unknown format: {format}")
