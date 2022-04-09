import json
from ..client import client
from ..utils import confirm


class GetClass:
    def __init__(self):
        """ GetClass __init__ """

    def pages(self, page_ids, indent=None, label="current"):
        """ Retrieve page objects.

        Args:
            page_ids (_type_): Page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving page information.
        """
        c = client.Client(label)
        ret = []
        for page_id in page_ids.split():
            ret.append(json.loads(c.get_page(page_id)))

        return json.dumps(ret, indent=indent)

    def page_properties(self, page_ids, property_id, page_size=100, start_cursor="", indent=None, label="current"):
        """ Retrieve page properties.

        Args:
            page_ids (_type_): Page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            property_id (_type_): Property id.
            page_size (int, optional): The number of items to be obtained. Defaults to 100.
            start_cursor (str, optional): Starting position of the items to be acquired. Defaults to "".
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving page properties.
        """
        c = client.Client(label)
        ret = []
        for page_id in page_ids.split():
            ret.append(json.loads(c.get_page_property(
                page_id, property_id, page_size, start_cursor)))

        return json.dumps(ret, indent=indent)

    def databases(self, database_ids, indent=None, label="current"):
        """ Retrieve database objects.

        Args:
            database_ids (_type_): Database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"')
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving database objects.
        """
        c = client.Client(label)
        ret = []
        for database_id in database_ids.split():
            ret.append(json.loads(c.get_database(database_id)))

        return json.dumps(ret, indent=indent)

    def blocks(self, block_ids, indent=None, label="current"):
        """ Retrieve block objects.

        Args:
            block_ids (_type_): Block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving block objects.
        """
        c = client.Client(label)
        ret = []
        for block_id in block_ids.split():
            ret.append(json.loads(c.get_block(block_id)))

        return json.dumps(ret, indent=indent)

    def block_children(self, block_ids, page_size=100, start_cursor="", indent=None, label="current"):
        """ Retrieve block children.

        Args:
            block_ids (_type_): Parent block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            page_size (int, optional): The number of items to be obtained. Defaults to 100.
            start_cursor (str, optional): Starting position of the items to be acquired. Defaults to "".
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving block children.
        """
        c = client.Client(label)
        ret = []
        for block_id in block_ids.split():
            ret.append(json.loads(c.get_block_children(
                block_id, page_size, start_cursor)))

        return json.dumps(ret, indent=indent)

    def users(self, user_ids, indent=None, label="current"):
        """ Retrieve user objects.

        Args:
            user_ids (_type_): User ids (e.g. '--user-ids="xxxxxxxxxx yyyyyyyyyy"')
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving user objects.
        """
        c = client.Client(label)
        ret = []
        for user_id in user_ids.split():
            ret.append(json.loads(c.get_user(user_id)))

        return json.dumps(ret, indent=indent)

    def all_users(self, page_size=100, start_cursor="", indent=None, label="current"):
        """ Retrieve all user objects.

        Args:
            page_size (int, optional): The number of items to be obtained. Defaults to 100.
            start_cursor (str, optional): Starting position of the items to be acquired. Defaults to "".
            indent (_type_, optional): Indent width of json. Defaults to None.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Result of retrieving all user objects.
        """
        c = client.Client(label)
        ret = json.loads(c.get_all_user(page_size, start_cursor))

        return json.dumps(ret, indent=indent)
