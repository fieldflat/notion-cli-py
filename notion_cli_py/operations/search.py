import json
from ..client import client

class SearchClass:
    def __init__(self):
        """ SearchClass __init__ """

    def data(self, read_path, label="current"):
        c = client.Client(label)
        payload = json.load(open(read_path, 'r'))
        ret = json.loads(c.search(payload))
        return json.dumps(ret)