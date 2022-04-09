import json
from ..client import client
from ..utils import confirm


class DeleteClass:
    def __init__(self):
        """ DeleteClass __init__ """

    def blocks(self, block_ids, noconfirm=False, label="current"):
        """ Delete block objects.

        Args:
            block_ids (_type_): Parent block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of deleting block objects.
        """
        c = client.Client(label)

        ret = []
        for block_id in block_ids.split():
            contents = [("block_id", block_id)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                ret.append(json.loads(c.delete_block(block_id)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)
