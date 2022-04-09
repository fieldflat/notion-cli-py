import json
from typing import Dict
from ..client import client
import sys
import re
from ..utils import read_file, confirm
from tabulate import tabulate

class CreateClass:
    def __init__(self):
        """ CreateClass __init__ """

    def pages(self, page_ids, template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """ Create pages to existing parent page.

        Args:
            page_ids (str, optional): Parent page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for page object. Defaults to "simple_page".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of creating pages.
        """
        c = client.Client(label)

        ret = []
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                payload["parent"] = {
                    "page_id": page_id,
                }
                ret.append(json.loads(c.create_page(payload)))
        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def pages_to_database(self, database_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """ Create pages to existing parent database.

        Args:
            database_ids (_type_): Parent database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for page object. Defaults to "simple_database".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            _type_: _description_
        """
        c = client.Client(label)

        ret = []
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                payload["parent"] = {
                    "database_id": database_id,
                }
                ret.append(json.loads(c.create_page(payload)))
        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, page_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """ Create databases to existing parent page.

        Args:
            page_ids (_type_): Parent page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for page object. Defaults to "simple_database".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of creating databases.
        """
        c = client.Client(label)

        ret = []
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template name", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(template_name)
                payload["parent"] = {
                    "type": "page_id",
                    "page_id": page_id,
                }
                ret.append(json.loads(c.create_database(payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)