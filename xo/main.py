import threading
import time

from xo.input_output.console import Console
from xo.mark_enum import Mark


def main():
    screen = Console()
    thread = threading.Thread(target=screen.start_game)
    thread.start()
    time.sleep(5)
    screen.mark((1, 1), Mark.Ex)
    time.sleep(5)
    screen.stop_game()


if __name__ == "__main__":
    main()
