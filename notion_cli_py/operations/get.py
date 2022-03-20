import json
from ..client import client

class GetClass:
    def __init__(self):
        """ GetClass __init__ """

    def pages(self, page_ids, write_path=None, indent=4, label="current"):
        """ get pages information """
        c = client.Client(label)
        ret = []
        for page_id in page_ids.split():
            ret.append(json.loads(c.get_page(page_id)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def page_properties(self, page_ids, property_id, write_path=None, indent=4, label="current"):
        """ get pages information """
        c = client.Client(label)
        ret = []
        for page_id in page_ids.split():
            ret.append(json.loads(c.get_page_property(page_id, property_id)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def databases(self, database_ids, write_path=None, indent=4, label="current"):
        """ get databases information """
        c = client.Client(label)
        ret = []
        for database_id in database_ids.split():
            ret.append(json.loads(c.get_database(database_id)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def blocks(self, block_ids, write_path=None, indent=4, label="current"):
        """ get blocks information """
        c = client.Client(label)
        ret = []
        for block_id in block_ids.split():
            ret.append(json.loads(c.get_block(block_id)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def block_children(self, block_ids, page_size=100, write_path=None, indent=4, label="current"):
        """ get block children """
        c = client.Client(label)
        ret = []
        for block_id in block_ids.split():
            ret.append(json.loads(c.get_block_children(block_id, page_size)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def users(self, user_ids, write_path=None, indent=4, label="current"):
        """ get users information """
        c = client.Client(label)
        ret = []
        for user_id in user_ids.split():
            ret.append(json.loads(c.get_user(user_id)))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)

    def all_users(self, page_size=100, write_path=None, indent=4, label="current"):
        """ get all users information """
        c = client.Client(label)
        ret = json.loads(c.get_all_user(page_size))

        if write_path is None:
            return json.dumps(ret, indent=indent)
        else:
            with open(write_path, 'w') as f:
                json.dump(ret, f, indent=indent)
        return json.dumps(ret)