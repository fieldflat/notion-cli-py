import json
from ..client import client
from ..utils import read_file
from tabulate import tabulate
import sys

class AppendClass:
    def __init__(self):
        """ AppendClass __init__ """

    def block_children(self, block_ids="", template_name="simple_block", read_path=None, noconfirm=False, label="current"):
        """ update block children """
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
                    ret.append(json.loads(c.append_block_children(block_id, payload)))
                    break
                elif choice in ['n', 'no']:
                    print("==> Skipped.")
                    break
            if noconfirm:
                ret.append(json.loads(c.append_block_children(block_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)