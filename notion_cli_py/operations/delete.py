import json
from ..client import client
from ..utils import confirm

class DeleteClass:
    def __init__(self):
        """ DeleteClass __init__ """

    def blocks(self, block_ids, noconfirm=False, label="current"):
        """ delete blocks """
        c = client.Client(label)

        ret = []
        for block_id in block_ids.split():
            contents = [("block_id", block_id)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                ret.append(json.loads(c.delete_block(block_id)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)