import json
from ..client import client
from ..utils import read_file, confirm
from tabulate import tabulate
import sys

class UpdateClass:
    def __init__(self):
        """ UpdateClass __init__ """

    def pages(self, page_ids, template_name="simple_page", read_path=None, noconfirm=False, label="current"):
        """
        update pages
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
                ret.append(json.loads(c.update_page(page_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def databases(self, database_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current"):
        """
        update databases
        """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                ret.append(json.loads(c.update_database(database_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)

    def blocks(self, block_ids, template_name="simple_update_block", read_path=None, noconfirm=False, label="current"):
        """
        update blocks
        """
        c = client.Client(label)

        ### load template
        if read_path is None:
            read_path = read_file.read_template_file(template_name)
        payload = json.load(open(read_path, 'r'))

        ret = []
        for block_id in block_ids.split():
            contents = [("block_id", block_id), ("template path", read_path)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                ret.append(json.loads(c.update_block(block_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)