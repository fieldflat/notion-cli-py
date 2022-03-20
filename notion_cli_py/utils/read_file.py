import os

def read_template_file(template_name: str):
    read_path = "../../files/" + template_name + ".json"
    base = os.path.dirname(os.path.abspath(__file__))
    read_path = os.path.normpath(os.path.join(base, read_path))

    return read_path