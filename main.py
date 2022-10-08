import threading
import time

from mark_enum import Mark
from screen.cli_screen import CLIScreen


def main():
    screen = CLIScreen()
    thread = threading.Thread(target=screen.start)
    thread.start()
    time.sleep(5)
    screen.fill_location((1, 1), Mark.X)
    time.sleep(5)
    screen.stop()

if __name__ == "__main__":
    main()