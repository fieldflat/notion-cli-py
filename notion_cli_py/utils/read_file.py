import sys
import requests
import json


def read_template_file(template_name: str):
    try:
        url = "https://raw.githubusercontent.com/fieldflat/notion-cli-py/main/files/" + \
            template_name + ".json"
        print("===> fetching {url}".format(url=url))
        response = requests.get(url)
        jsonData = response.json()
        return jsonData
    except json.JSONDecodeError:
        print("something wrong...", file=sys.stderr)
        print("fetching template: {template_name} does not work...".format(
            template_name=template_name), file=sys.stderr)
        sys.exit(1)
