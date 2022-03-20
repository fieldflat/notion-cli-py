import json
from typing import Dict
from ..client import client
import sys
import re
from ..utils import read_file
from tabulate import tabulate

class DeleteClass:
    def __init__(self):
        """ DeleteClass __init__ """

    def blocks(self, block_ids, read_path=None, noconfirm=False, label="current"):
        """ delete blocks """
        c = client.Client(label)

        ret = []
        for block_id in block_ids.split():
            while True and (not noconfirm):
                contents = [("block_id", block_id)]
                print(tabulate(contents, headers=["key", "value"], tablefmt='fancy_grid'))
                choice = input("is OK? [y/N]: ").lower()
                if choice in ['y', 'ye', 'yes']:
                    ret.append(json.loads(c.delete_block(block_id)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)