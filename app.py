import os
import threading
from library.Logging import *
from library.openshift import *

#if "OPENSHIFT_BUILD_NAME" in os.environ:
#    from library.openshift import *
#else:
#    raise ValueError("Don't run on openshift or Kubernetes")


def main():
    t1 = threading.Thread(target=watch_nodes, args=("WatchNodes", "Node"), daemon=True, name='WatchNodes')
    t1.start()
    t1.join()
    t2 = threading.Thread(target=get_nodes, args=("GetNodes", "Node"), daemon=True, name='GetNodes')
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
