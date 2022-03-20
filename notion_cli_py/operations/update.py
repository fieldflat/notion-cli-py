import json
from ..client import client
from ..utils import read_file
from tabulate import tabulate
import sys

class UpdateClass:
    def __init__(self):
        """ UpdateClass __init__ """

    def pages(self, page_ids="", template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """ update pages """
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
                    ret.append(json.loads(c.update_page(page_id, payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, database_ids="", template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """ update databases """
        c = client.Client(label)
        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for database_id in database_ids.split():
            while True and (not noconfirm):
                contents = [("database_id", database_id), ("template path", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    ret.append(json.loads(c.update_database(database_id, payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def blocks(self, block_ids="", template_name="simple_block", read_path=None, noconfirm=False, label="current"):
        """ update blocks """
        c = client.Client(label)
        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for block_id in block_ids.split():
            while True and (not noconfirm):
                contents = [("block_id", block_id), ("template path", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    ret.append(json.loads(c.update_block(block_id, payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)