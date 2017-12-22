import os
import json

DATA = os.path.join(os.path.dirname(__file__), 'eo_lookup_revo.json')


def get_content():
    with open(DATA, 'r') as f:
        return json.loads(f.read())
