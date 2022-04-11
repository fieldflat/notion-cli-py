import toml
import os
import requests
import sys
from ..utils import logger


class Client:
    def __init__(self, label):
        self.logger = logger.init_logger()
        try:
            PATH = os.environ['HOME'] + "/.notion_cli/config.toml"
            config = toml.load(open(PATH))
            self.config = config[label]
        except FileNotFoundError:
            self.logger.error("[ERR] Not Found config file ({PATH}).".format(PATH=PATH))
            self.logger.error("      You need to create config file before utilizing notion-cli operations.")
            self.logger.error("      Please execute following command.")
            self.logger.error("        *  notion-cli configure set")
            sys.exit(1)
        except KeyError:
            self.logger.error("[ERR] Not found label ({label}).".format(label=label))
            self.logger.error("      To create label, please execute following command.")
            self.logger.error("        * notion-cli configure set")
            sys.exit(1)

    def get_headers(self):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Notion-Version": self.config["notion_api_version"],
            "Authorization": "Bearer {token}".format(token=self.config["token"])
        }
        return headers

    def get_page(self, page_id):
        """ get_page """
        url = "https://api.notion.com/v1/pages/{page_id}".format(
            page_id=page_id)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def get_page_property(self, page_id, property_id, page_size, start_cursor):
        """ get page property """
        url = "https://api.notion.com/v1/pages/{page_id}/properties/{property_id}?page_size={page_size}".format(
            page_id=page_id, property_id=property_id, page_size=page_size)
        if start_cursor:
            url += "&start_cursor={start_cursor}".format(
                start_cursor=start_cursor)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def create_page(self, payload):
        url = "https://api.notion.com/v1/pages"
        headers = self.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)

        return response.text

    def update_page(self, page_id, payload):
        url = "https://api.notion.com/v1/pages/{page_id}".format(
            page_id=page_id)
        headers = self.get_headers()
        response = requests.request(
            "PATCH", url, json=payload, headers=headers)

        return response.text

    def get_database(self, database_id):
        url = "https://api.notion.com/v1/databases/{database_id}".format(
            database_id=database_id)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def create_database(self, payload):
        url = "https://api.notion.com/v1/databases"
        headers = self.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)

        return response.text

    def update_database(self, database_id, payload):
        url = "https://api.notion.com/v1/databases/{database_id}".format(
            database_id=database_id)
        headers = self.get_headers()
        response = requests.request(
            "PATCH", url, json=payload, headers=headers)

        return response.text

    def query_database(self, database_id, payload):
        url = "https://api.notion.com/v1/databases/{database_id}/query".format(
            database_id=database_id)
        headers = self.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)

        return response.text

    def get_block(self, block_id):
        url = "https://api.notion.com/v1/blocks/{block_id}".format(
            block_id=block_id)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def get_block_children(self, block_id, page_size, start_cursor):
        url = "https://api.notion.com/v1/blocks/{block_id}/children?page_size={page_size}".format(
            block_id=block_id, page_size=page_size)
        if start_cursor:
            url += "&start_cursor={start_cursor}".format(
                start_cursor=start_cursor)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def update_block(self, block_id, payload):
        url = "https://api.notion.com/v1/blocks/{block_id}".format(
            block_id=block_id)
        headers = self.get_headers()
        response = requests.request(
            "PATCH", url, json=payload, headers=headers)

        return response.text

    def delete_block(self, block_id):
        url = "https://api.notion.com/v1/blocks/{block_id}".format(
            block_id=block_id)
        headers = self.get_headers()
        response = requests.request("DELETE", url, headers=headers)

        return response.text

    def append_block_children(self, block_id, payload):
        url = "https://api.notion.com/v1/blocks/{block_id}/children".format(
            block_id=block_id)
        headers = self.get_headers()
        response = requests.request(
            "PATCH", url, json=payload, headers=headers)

        return response.text

    def get_user(self, user_id):
        url = "https://api.notion.com/v1/users/{user_id}".format(
            user_id=user_id)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def get_all_user(self, page_size, start_cursor):
        url = "https://api.notion.com/v1/users?page_size={page_size}".format(
            page_size=page_size)
        if start_cursor:
            url += "&start_cursor={start_cursor}".format(
                start_cursor=start_cursor)
        headers = self.get_headers()
        response = requests.request("GET", url, headers=headers)

        return response.text

    def search(self, payload):
        url = "https://api.notion.com/v1/search"
        headers = self.get_headers()
        response = requests.request("POST", url, json=payload, headers=headers)

        return response.text
