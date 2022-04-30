from tabulate import tabulate
from ..utils import input_handler


def confirm(contents, headers=["key", "value"], tablefmt='fancy_grid', noconfirm=False):
    if not noconfirm:
        print(tabulate(contents, headers=headers, tablefmt=tablefmt))
    while True and (not noconfirm):
        choice = input_handler.input_handler("is OK? [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            print("==> Skipped.")
            return False

    # return True if noconfirm is True
    return True
