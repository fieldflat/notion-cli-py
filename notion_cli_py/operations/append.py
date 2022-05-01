import json
import sys
from ..client import client
from ..utils import read_file, confirm, logger
from logging import getLogger, DEBUG, StreamHandler, INFO


class AppendClass:
    def __init__(self):
        """ AppendClass __init__ """
        self.logger = logger.init_logger(__name__)

    def block_children(self, block_ids, template_name="simple_block", read_path=None, noconfirm=False, label="current", debug=False):
        """ Append block children to existing parent block.

        Args:
            block_ids (str): Parent block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for block object. Defaults to "simple_block".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of appending block children.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(
            read_path, 'r')) if read_path else read_file.read_template_file(template_name, self.logger)
        for block_id in block_ids.split():
            contents = [("block_id", block_id), ("template path",
                                                 read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                response_json = json.loads(
                    c.append_block_children(block_id, payload))
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
