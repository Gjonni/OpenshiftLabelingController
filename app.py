import os
import _thread
from library.Logging import *
from library.openshift import *






def main():
    Logging.logger.info(f"Verifico....")
    _thread.start_new_thread(ocp, ("Nodes-Thread", 2, "Node"))

    while 1:
        pass


if __name__ == "__main__":
    main()



