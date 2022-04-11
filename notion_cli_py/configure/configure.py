from getpass import getpass
import toml
import os
import sys
from tabulate import tabulate
from ..utils import confirm, logger
from notion_cli_py import __version__


class ConfigureClass:
    def __init__(self):
        """ Configure __init__ """
        DIR = os.environ['HOME'] + "/.notion_cli"
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        self.logger = logger.init_logger()
        if not os.path.exists(DIR) or not os.path.exists(PATH):
            self.logger.info(
                """
_____   __     __________             ______________________
___  | / /_______  /___(_)______________  ____/__  /____  _/
__   |/ /_  __ \  __/_  /_  __ \_  __ \  /    __  /  __  /  
_  /|  / / /_/ / /_ _  / / /_/ /  / / / /___  _  /____/ /   
/_/ |_/  \____/\__/ /_/  \____//_/ /_/\____/  /_____/___/   
                """
            )
            self.logger.info("Version {version}".format(version=__version__))
            yn = input(
                "Are you sure to create config file in {DIR}? [y/N]: ".format(DIR=DIR))
            if yn != "y":
                self.logger.error("==> Aborted.")
                sys.exit(0)
            if not os.path.exists(DIR):
                self.logger.info("creating directory '{DIR}' ... ".format(DIR=DIR))
                os.mkdir(DIR)
                self.logger.info("==> Done.")
            if not os.path.exists(PATH):
                self.logger.info("creating file '{PATH}' ... ".format(PATH=PATH))
                try:
                    with open(PATH, "x") as f:
                        self.logger.info("==> Done.")
                except FileExistsError:
                    self.logger.error("'{PATH}' already exists.".format(
                        PATH=PATH), file=sys.stderr)
                    sys.exit(1)
        config = toml.load(open(PATH))
        self.config = config

    def set(self, label=None, token=None, notion_api_version=None, noconfirm=False):
        """ Set your integration information.
        You need to create Internal Integration Token before executing this command.

        Args:
            label (_type_, optional): Name to identify your integration. Defaults to None.
            token (_type_, optional): Internal Integration Token. Defaults to None.
            notion_api_version (_type_, optional): Notion API Version. Defaults to None.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
        """
        if label is None:
            label = input("input config label name: ")
        if token is None:
            token = getpass('input token for {label}: '.format(label=label))
        if notion_api_version is None:
            notion_api_version = input(
                "input notion api version [2022-02-22]: ")
            if notion_api_version == "" or notion_api_version == None:
                notion_api_version = "2022-02-22"

        conf = {
            "label": label,
            "token": token,
            "notion_api_version": notion_api_version,
        }

        # confirm settings
        contents = [(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:])
                    for k, v in conf.items()]
        if not confirm.confirm(contents, noconfirm=noconfirm):
            sys.exit(0)

        # confirm override
        if label in self.config:
            while True and (not noconfirm):
                choice = input(
                    "Label ('{label}') is already registered. Do you really override? [y/N]: ".format(label=label)).lower()
                if choice in ['y', 'ye', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    self.logger.error("==> Aborted.")
                    sys.exit(0)

        # write settings
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        self.config[label] = conf
        toml.dump(self.config, open(PATH, mode='w'))
        self.logger.info("==> Done.")

        # confirm override
        if label in self.config:
            while True and (not noconfirm):
                choice = input(
                    "Do you want to set label ('{label}') to current label? [y/N]: ".format(label=label)).lower()
                if choice in ['y', 'ye', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    self.logger.error("==> Exit.")
                    sys.exit(0)

        self.config["current"] = conf
        toml.dump(self.config, open(PATH, mode='w'))
        self.logger.info("==> Done.")

    def show(self, label=""):
        """ Show your integration information.

        Args:
            label (str, optional): Label name for your integration information. Defaults to "current".
        """
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"

        if label == "":
            for key in self.config:
                if key == "current":
                    continue
                prefix = "  * " if self.config["current"]["label"] == self.config[key]["label"] else "    "
                self.logger.info(prefix + key)
            sys.exit(0)

        if label in self.config:
            self.logger.info(tabulate([(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:])
                  for k, v in self.config[label].items()], headers=["key", "value"], tablefmt='fancy_grid'))
            self.logger.info("is current label:",
                  True if self.config["current"]["label"] == self.config[label]["label"] else False)
        else:
            self.logger.error("Label: '{label}' does not exist in {path}".format(
                label=label, path=PATH))
            sys.exit(1)

    def switch(self, label, noconfirm=False):
        """ Switch integration setting.

        Args:
            label (_type_): Label name for your integration information.
            noconfirm (bool, optional): If you need not to confirm, set '--noconfirm=True' option. Defaults to False.
        """
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"

        if label in self.config:
            contents = [(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:])
                        for k, v in self.config[label].items()]
            if confirm.confirm(contents, noconfirm=noconfirm):
                self.config["current"] = self.config[label]
                toml.dump(self.config, open(PATH, mode='w'))
                self.logger.info("==> switched.")
        else:
            self.logger.error("Label: '{label}' does not exist in {path}".format(
                label=label, path=PATH))
            sys.exit(1)
