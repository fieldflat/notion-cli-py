import json
from ..client import client


class QueryClass:
    def __init__(self):
        """ QueryClass __init__ """

    def databases(self, database_ids, read_path, page_size=100, start_cursor="", indent=None, label="current"):
        """ Querying the database.

        Args:
            database_ids (_type_): Parent database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"').
            read_path (_type_): Read path for query file
            page_size (int, optional): The number of items to be obtained. Defaults to 100.
            start_cursor (str, optional): Starting position of the items to be acquired. Defaults to "".
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of querying the database.
        """
        c = client.Client(label)

        # load template
        payload = json.load(open(read_path, 'r'))

        ret = []
        for database_id in database_ids.split():
            payload["page_size"] = page_size
            if start_cursor != "":
                payload["start_cursor"] = start_cursor
            ret.append(json.loads(c.query_database(database_id, payload)))

        return json.dumps(ret, indent=indent)
