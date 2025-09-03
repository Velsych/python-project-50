import json

import yaml


def file_parser(file_path):
    if file_path.endswith(".json"):
        return json.load(open(file_path))
    if file_path.endswith(".yml") or file_path.endswith(".yaml"):
        return yaml.load(open(file_path), yaml.Loader)


