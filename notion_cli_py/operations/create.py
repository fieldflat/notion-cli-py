import json
import logging
from typing import Dict
from ..client import client
import sys
import re
from ..utils import logger, read_file, confirm
from tabulate import tabulate
from logging import getLogger, DEBUG, StreamHandler, INFO


class CreateClass:
    def __init__(self):
        """ CreateClass __init__ """
        self.logger = logger.init_logger()

    def pages(self, page_ids, template_name="simple_page", read_path=None, noconfirm=False, label="current", debug=False):
        """ Create pages to existing parent page.

        Args:
            page_ids (str, optional): Parent page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for page object. Defaults to "simple_page".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of creating pages.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(
            read_path, 'r')) if read_path else read_file.read_template_file(template_name, self.logger)
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template path", read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "page_id": page_id,
                }
                response_json = json.loads(c.create_page(payload))
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

    def pages_to_database(self, database_ids, template_name="simple_page", read_path=None, noconfirm=False, label="current", debug=False):
        """ Create pages to existing parent database.

        Args:
            database_ids (_type_): Parent database ids (e.g. '--database-ids="xxxxxxxxxx yyyyyyyyyy"').
            template_name (str, optional): Template name for page object. Defaults to "simple_database".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            _type_: _description_
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(read_path, 'r')) if read_path else read_file.read_template_file(
            template_name, self.logger)
        for database_id in database_ids.split():
            contents = [("database_id", database_id), ("template path",
                                                       read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "database_id": database_id,
                }
                response_json = json.loads(c.create_page(payload))
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

    def databases(self, page_ids, template_name="simple_database", read_path=None, noconfirm=False, label="current", debug=False):
        """ Create databases to existing parent page.

        Args:
            page_ids (_type_): Parent page ids (e.g. '--page-ids="xxxxxxxxxx yyyyyyyyyy"')
            template_name (str, optional): Template name for page object. Defaults to "simple_database".
            read_path (_type_, optional): Read path for input template file. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
            label (str, optional): Name to identify your integration. Defaults to "current".
            debug (bool, optional): If you need debug messages, set '--debug' option. Defaults to False.

        Returns:
            json: Results of creating databases.
        """
        c = client.Client(label)
        if debug:
            self.logger.setLevel(DEBUG)

        ret = []
        payload = json.load(open(
            read_path, 'r')) if read_path else read_file.read_template_file(template_name, self.logger)
        for page_id in page_ids.split():
            contents = [("page_id", page_id), ("template name",
                                               read_path if read_path else template_name)]
            if confirm.confirm(contents, noconfirm=noconfirm):
                payload["parent"] = {
                    "type": "page_id",
                    "page_id": page_id,
                }
                response_json = json.loads(c.create_database(payload))
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
