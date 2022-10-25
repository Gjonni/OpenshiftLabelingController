import os
import threading 
from library.Logging import *
from library.openshift import *


def main():
    t1 = threading.Thread(target=watch_nodes, args=(("Node")), daemon=True, name='WatchNodes')
    t2 = threading.Thread(target=get_nodes, args=("Node"), daemon=True, name='GetNodes')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()


