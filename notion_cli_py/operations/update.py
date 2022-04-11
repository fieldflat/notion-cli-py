import json
from ..client import client
from ..utils import read_file, confirm, logger
from tabulate import tabulate
import sys
from logging import getLogger, DEBUG, StreamHandler, INFO


class UpdateClass:
    def __init__(self):
        """ UpdateClass __init__ """
        self.logger = logger.init_logger()

    def pages(self, page_ids, template_name="simple_update_page", read_path=None, noconfirm=False, label="current", debug=False):
        """ Updating page objects.

        Args:
            page_ids (_type_): Page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for page object. Defaults to "simple_page".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of updating page objects.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(
            read_path, 'r')) if read_path else read_file.read_template_file(template_name, self.logger)
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template path",
                                               read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                response_json = json.loads(c.update_page(page_id, payload))
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

    def databases(self, database_ids, template_name="simple_update_database", read_path=None, noconfirm=False, label="current", debug=False):
        """ Updating database objects.

        Args:
            database_ids (_type_): Database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for database object. Defaults to "simple_database".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of updating database objects.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(
            read_path, 'r')) if read_path else read_file.read_template_file(template_name, self.logger)
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path",
                                                       read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                response_json = json.loads(c.update_database(database_id, payload))
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


    def blocks(self, block_ids, template_name="simple_update_block", read_path=None, noconfirm=False, label="current", debug=False):
        """ Updating block objects.

        Args:
            block_ids (_type_): block ids (e.g. '--block-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for block object. Defaults to "simple_update_block".
            read_path (str, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of updating block objects.
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
                response_json = json.loads(c.update_block(block_id, payload))
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
