from tabulate import tabulate

def confirm(contents, headers=["key", "value"], tablefmt='fancy_grid', noconfirm=False):
    while True and (not noconfirm):
        print(tabulate(contents, headers=headers, tablefmt=tablefmt))
        choice = input("is OK? [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            print("==> Skipped.")
            return False

    # return True if noconfirm is True
    return True