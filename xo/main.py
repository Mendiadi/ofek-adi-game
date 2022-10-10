import threading
import time
from io.console import CLIScreen

from mark_enum import Mark


def main():
    screen = CLIScreen()
    thread = threading.Thread(target=screen.start)
    thread.start()
    time.sleep(5)
    screen.fill_location((1, 1), Mark.Ex)
    time.sleep(5)
    screen.stop()


if __name__ == "__main__":
    main()
