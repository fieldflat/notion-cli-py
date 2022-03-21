import json
from ..client import client

class SearchClass:
    def __init__(self):
        """ SearchClass __init__ """

    def data(self, read_path, page_size=100, start_cursor="", write_path=None, indent=None, label="current"):
        c = client.Client(label)
        payload = json.load(open(read_path, 'r'))
        payload["page_size"] = page_size
        if start_cursor != "":
            payload["start_cursor"] = start_cursor
        ret = json.loads(c.search(payload))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                return json.dump(ret, f, indent=indent)
