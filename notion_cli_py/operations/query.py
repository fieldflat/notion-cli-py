import json
from ..client import client

class QueryClass:
    def __init__(self):
        """ QueryClass __init__ """

    def databases(self, database_ids, read_path, page_size=100, start_cursor="", write_path=None, indent=None, label="current"):
        """ query databases """
        c = client.Client(label)

        ### load template
        payload = json.load(open(read_path, 'r'))

        ret = []
        for database_id in database_ids.split():
            payload["page_size"] = page_size
            if start_cursor != "":
                payload["start_cursor"] = start_cursor
            ret.append(json.loads(c.query_database(database_id, payload)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                return json.dump(ret, f, indent=indent)