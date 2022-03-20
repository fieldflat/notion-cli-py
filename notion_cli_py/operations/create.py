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

    def pages(self, page_ids="", database_ids="", template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """
        create pages
        """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template path", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "page_id": page_id,
                }
                ret.append(json.loads(c.create_page(payload)))
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "database_id": database_id,
                }
                ret.append(json.loads(c.create_page(payload)))
        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, page_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """
        create a single database
        """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template name", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "type": "page_id",
                    "page_id": page_id,
                }
                ret.append(json.loads(c.create_database(payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)