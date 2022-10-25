import os
import _thread
from library.Logging import *
from library.openshift import *
import schedule
import threading
import time





def main():
    Logging.logger.info(f"Verifico....")
    _thread.start_new_thread(watch_nodes, ("Nodes-Thread", 2, "Node"))

    while 1:
        pass


if __name__ == "__main__":
    main()


