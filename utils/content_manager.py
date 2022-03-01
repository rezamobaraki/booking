import json


def get_errors(content):
    errors = content.get('detail')
    json_error = dict()
    for error in errors:
        json_error[error.get('loc')[1]] = error.get('msg')
    return json.dumps(json_error, indent=4)
