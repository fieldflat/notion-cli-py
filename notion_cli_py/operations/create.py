import json
from typing import Dict
from ..client import client
import sys
import re
from ..utils import read_file
from tabulate import tabulate

class CreateClass:
    def __init__(self):
        """ CreateClass __init__ """

    def pages(self, page_ids="", database_ids="", template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """ create pages """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for page_id in page_ids.split():
            while True and (not noconfirm):
                contents = [("page_id", page_id), ("template path", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    payload["parent"] = {
                        "page_id": page_id,
                    }
                    ret.append(json.loads(c.create_page(payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break
        for database_id in database_ids.split():
            # confirm settings
            while True and (not noconfirm):
                contents = [("database_id", database_id), ("template path", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    payload["parent"] = {
                        "database_id": database_id,
                    }
                    ret.append(json.loads(c.create_page(payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break
        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, page_ids="", template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """ create a single database """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for page_id in page_ids.split():
            while True and (not noconfirm):
                contents = [("page_id", page_id), ("template name", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    payload["parent"] = {
                        "page_id": page_id,
                    }
                    ret.append(json.loads(c.create_database(payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)