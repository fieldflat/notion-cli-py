import json
from ..client import client
from ..utils import confirm, logger
from logging import getLogger, DEBUG, StreamHandler, INFO


class DeleteClass:
    def __init__(self):
        """ DeleteClass __init__ """
        self.logger = logger.init_logger()

    def blocks(self, block_ids, noconfirm=False, label="current", debug=False):
        """ Delete block objects.

        Args:
            block_ids (_type_): Parent block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of deleting block objects.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        for block_id in block_ids.split():
            contents = [("block_id", block_id)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                response_json = json.loads(c.delete_block(block_id))
                if not noconfirm:
                    if response_json["object"] == "error":
                        self.logger.error("===> NG")
                        self.logger.error(response_json)
                    else:
                        self.logger.info("===> Done")
                        self.logger.debug(response_json)
                ret.append(response_json)

        if noconfirm:
            self.logger.info(json.dumps(ret))
