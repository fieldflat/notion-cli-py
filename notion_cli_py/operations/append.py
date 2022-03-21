import json
from ..client import client
from ..utils import read_file, confirm

class AppendClass:
    def __init__(self):
        """ AppendClass __init__ """

    def block_children(self, block_ids, template_name="simple_block", read_path=None, noconfirm=False, label="current"):
        """ Append block children to existing parent block.

        Args:
            block_ids (str): Parent block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for block object. Defaults to "simple_block".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".

        Returns:
            json: Results of appending block children.
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
                ret.append(json.loads(c.append_block_children(block_id, payload)))

        return json.dumps(ret) if len(ret) != 0 else sys.exit(0)