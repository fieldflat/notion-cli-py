import os
import requests
import json

def read_template_file(template_name: str):
    url = "https://raw.githubusercontent.com/fieldflat/notion-cli-py/main/files/" + template_name + ".json"
    response = requests.get(url)
    jsonData = response.json()

    return jsonData