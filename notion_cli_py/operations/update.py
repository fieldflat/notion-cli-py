import json
from ..client import client
from ..utils import read_file, confirm
from tabulate import tabulate
import sys

class UpdateClass:
    def __init__(self):
        """ UpdateClass __init__ """

    def pages(self, page_ids, template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """ Updating page objects.

        Args:
            page_ids (_type_): Page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for page object. Defaults to "simple_page".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of updating page objects.
        """
        c = client.Client(label)

        ret = []
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                ret.append(json.loads(c.update_page(page_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, database_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """ Updating database objects.

        Args:
            database_ids (_type_): Database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for database object. Defaults to "simple_database".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of updating database objects.
        """
        c = client.Client(label)

        ret = []
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                ret.append(json.loads(c.update_database(database_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def blocks(self, block_ids, template_name="simple_update_block", read_path=None, noconfirm=False, label="current"):
        """ Updating block objects.

        Args:
            block_ids (_type_): block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for block object. Defaults to "simple_update_block".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of updating block objects.
        """
        c = client.Client(label)

        ret = []
        for block_id in block_ids.split():
            contents = [("block_id", block_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                ret.append(json.loads(c.update_block(block_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)