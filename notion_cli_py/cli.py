import fire
from .configure import configure
from .operations import create, get, update, search, append, delete, query


class Command(object):
    def get(self):
        """ Getting (Retrieving) operations.

        Returns:
            _type_: Result of get operations.
        """
        return get.GetClass()

    def create(self):
        """ Creating operations.

        Returns:
            _type_: Result of creating operations.
        """
        return create.CreateClass()

    def update(self):
        """ Updating operations.

        Returns:
            _type_: Result of updating operations.
        """
        return update.UpdateClass()

    def configure(self):
        """ Configuration operations.

        Returns:
            _type_: Result of configuration operations.
        """
        return configure.ConfigureClass()

    def search(self):
        """ Searching operations.

        Returns:
            _type_: Result of searching operations.
        """
        return search.SearchClass()

    def append(self):
        """ Appending operations.

        Returns:
            _type_: Result of appending operations.
        """
        return append.AppendClass()

    def delete(self):
        """ Deleting operations.

        Returns:
            _type_: Result of deleting operations.
        """
        return delete.DeleteClass()

    def query(self):
        """ Query operations.

        Returns:
            _type_: Result of query operations.
        """
        return query.QueryClass()


def main():
    fire.Fire(Command)
