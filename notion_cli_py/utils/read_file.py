import sys
import requests
import json


def read_template_file(template_name: str, logger):
    try:
        url = "https://raw.githubusercontent.com/fieldflat/notion-cli-py/main/files/" + \
            template_name + ".json"
        logger.debug("===> fetching {url} ...".format(url=url))
        response = requests.get(url)
        jsonData = response.json()
        return jsonData
    except json.JSONDecodeError:
        logger.error("something wrong...", file=sys.stderr)
        logger.error("fetching template: {template_name} does not work...".format(
            template_name=template_name), file=sys.stderr)
        sys.exit(1)
