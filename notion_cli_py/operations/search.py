import json
from ..client import client

class SearchClass:
    def __init__(self):
        """ SearchClass __init__ """

    def data(self, read_path, page_size=100, start_cursor="", write_path=None, indent=None, label="current"):
        """ Searching object data.

        Args:
            read_path (_type_): Read path for query file
            page_size (int, optional): The number of items to be obtained. Defaults to 100.
            start_cursor (str, optional): Starting position of the items to be acquired. Defaults to "".
            write_path (_type_, optional): Write path for output file. Defaults to None.
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of searching object data.
        """
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
