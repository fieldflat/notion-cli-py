import fire
from .configure import configure
from .operations import create, get, update, search, append, delete, query

class Command(object):
    def get(self):
        """ get operations """
        return get.GetClass()

    def create(self):
        """ create operations """
        return create.CreateClass()

    def update(self):
        """ update operations """
        return update.UpdateClass()

    def configure(self):
        """ configure operations """
        return configure.ConfigureClass()

    def search(self):
        """ search data """
        return search.SearchClass()

    def append(self):
        """ append data """
        return append.AppendClass()

    def delete(self):
        """ delete data """
        return delete.DeleteClass()

    def query(self):
        """ query data """
        return query.QueryClass()

def main():
    fire.Fire(Command)