import os
import threading 
from library.Logging import *
from library.openshift import *


def main():
    threading.Thread(target=watch_nodes, args=(("WatchNodes", "Node")), daemon=True, name='WatchNodes')
    threading.Thread(target=get_nodes, args=(("GetNodes", "Node")), daemon=True, name='GetNodes')


#    Logging.logger.info(f"Inizio la verifica degli host fisici di RHV su sui si trovano i nodi Openshift")
#    _thread.start_new_thread(watch_nodes, ("WatchNodes", 2, "Node"))


if __name__ == "__main__":
    main()


