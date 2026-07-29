import sys

from lib import exit_dialog, installer


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "exit":
        exit_dialog.main()
    else:
        installer.main()


if __name__ == "__main__":
    main()