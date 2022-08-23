import json
import yaml


def parser_content(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ('yml', 'ymal'):
        return yaml.safe_load(content)
    raise Exception(f'unknown format: {format}')
