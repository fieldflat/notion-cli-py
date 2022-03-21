from getpass import getpass
import toml
import os
import sys
from tabulate import tabulate
from ..utils import confirm

class ConfigureClass:
    def __init__(self):
        """ Configure __init__ """
        DIR = os.environ['HOME'] + "/.notion_cli"
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        if not os.path.exists(DIR):
            yn = input("Are you sure to create config file in {DIR}? [y/N]: ".format(DIR=DIR))
            if yn != "y":
                print("==> Done.")
                sys.exit(0)

            print("'{DIR}' directory does not exist.".format(DIR=DIR))
            print("creating directory '{DIR}' ... ".format(DIR=DIR))
            os.mkdir(DIR)
            print("==> Done.")
            print("creating file '{PATH}' ... ".format(PATH=PATH))
            try:
                with open(PATH, "x") as f:
                    print("==> Done.")
            except FileExistsError:
                print("'{PATH}' already exists.".format(PATH=PATH), file=sys.stderr)
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
            token = getpass('input token for {token}: '.format(token=token))
        if notion_api_version is None:
            notion_api_version = input("input notion api version [2022-02-22]: ")

        conf = {
            "label": label,
            "token": token,
            "notion_api_version": notion_api_version,
        }

        # confirm settings
        contents = [(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:]) for k, v in conf.items()]
        if not confirm.confirm(contents, noconfirm=noconfirm):
            sys.exit(0)

        # confirm override
        if label in self.config:
            while True and (not noconfirm):
                choice = input("Label ('{label}') is already registered. Do you really override? [y/N]: ".format(label=label)).lower()
                if choice in ['y', 'ye', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    print("==> Aborted.")
                    sys.exit(0)

        # write settings
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        self.config[label] = conf
        toml.dump(self.config, open(PATH, mode='w'))
        print("==> Done.")

        # confirm override
        if label in self.config:
            while True and (not noconfirm):
                choice = input("Do you want to set label ('{label}') to current label? [y/N]: ".format(label=label)).lower()
                if choice in ['y', 'ye', 'yes']:
                    break
                elif choice in ['n', 'no']:
                    print("==> Exit.")
                    sys.exit(0)

        self.config["current"] = conf
        toml.dump(self.config, open(PATH, mode='w'))
        print("==> Done.")

    def show(self, label="current"):
        """ Show your integration information.

        Args:
            label (str, optional): Label name for your integration information. Defaults to "current".
        """
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        config = toml.load(open(PATH))
        if label in config:
            print(tabulate([(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:]) for k, v in config[label].items()], headers=["key", "value"], tablefmt='fancy_grid'))
            print("is current label:", True if config["current"]["label"] == config[label]["label"] else False)
        else:
            print("Label: '{label}' does not exist in {path}".format(label=label, path=PATH))
            sys.exit(1)