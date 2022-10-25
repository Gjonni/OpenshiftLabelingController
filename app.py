import os
import _thread
from library.Logging import *
from library.openshift import *




def main():
    Logging.logger.info(f"Inizio la verifica degli host fisici di RHV su sui si trovano i nodi Openshift")
    _thread.start_new_thread(watch_nodes, ("WatchNodes", 2, "Node"))

    while 1:
        pass

if __name__ == "__main__":
    main()


