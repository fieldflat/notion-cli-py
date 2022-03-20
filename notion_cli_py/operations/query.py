import json
from typing import Dict
from ..client import client
import sys
import re
from ..utils import read_file
from tabulate import tabulate

class QueryClass:
    def __init__(self):
        """ QueryClass __init__ """

    def databases(self, database_ids, read_path, noconfirm=False, label="current"):
        """ query databases """
        c = client.Client(label)

        ### load template
        payload = json.load(open(read_path, 'r'))

        ret = []
        for database_id in database_ids.split():
            while True and (not noconfirm):
                contents = [("database_id", database_id), ("template name", read_path)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    ret.append(json.loads(c.query_database(database_id, payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break
            if noconfirm:
                ret.append(json.loads(c.query_database(database_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)