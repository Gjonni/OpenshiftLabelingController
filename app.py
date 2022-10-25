import os
import threading 
from library.Logging import *
from library.openshift import *


def main():
    threading.Thread(target=watch_nodes, args=("WatchNodes", "Node"), daemon=True, name='WatchNodes').start().join()
    threading.Thread(target=get_nodes, args=("GetNodes", "Node"), daemon=True, name='GetNodes').start().join()


if __name__ == "__main__":
    main()


