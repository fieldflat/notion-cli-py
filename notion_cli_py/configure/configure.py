from getpass import getpass
import toml
import os
import sys
from tabulate import tabulate

class ConfigureClass:
    def __init__(self):
        """ Configure __init__ """
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        config = toml.load(open(PATH))
        self.config = config

    def set(self, label=None, token=None, notion_api_version=None, noconfirm=False):
        if label is None:
            label = input("input config label name: ")
        if token is None:
            token = getpass('input token for {token}: '.format(token=token))
        if notion_api_version is None:
            notion_api_version = input("input notion api version: ")

        conf = {
            "label": label,
            "token": token,
            "notion_api_version": notion_api_version,
        }

        # confirm settings
        while True and (not noconfirm):
            print(tabulate([(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:]) for k, v in conf.items()], headers=["key", "value"], tablefmt='fancy_grid'))
            choice = input("is OK? [y/N]: ").lower()
            if choice in ['y', 'ye', 'yes']:
                break
            elif choice in ['n', 'no']:
                print("==> Aborted.")
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
        PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
        config = toml.load(open(PATH))
        if label in config:
            print(tabulate([(k, v if k != "token" else "*"*len(v[:-5]) + v[-5:]) for k, v in config[label].items()], headers=["key", "value"], tablefmt='fancy_grid'))
            print("Label: ", label)
        else:
            print("Label: '{label}' does not exist in {path}".format(label=label, path=PATH))
            sys.exit(1)