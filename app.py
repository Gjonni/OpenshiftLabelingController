import os
import _thread
from library.Logging import *
from library.openshift import *


def main():
    _thread.start_new_thread(watch_nodes, ("WatchNodes", "Node"))
    _thread.start_new_thread(get_nodes, ("GetNodes", "Node"))

#    Logging.logger.info(f"Inizio la verifica degli host fisici di RHV su sui si trovano i nodi Openshift")
#    _thread.start_new_thread(watch_nodes, ("WatchNodes", 2, "Node"))


if __name__ == "__main__":
    main()


