import os
from library.Logging import *
from library.openshift import *
import schedule
#import threading


#if "OPENSHIFT_BUILD_NAME" in os.environ:
#    from library.openshift import *
#else:
#    raise ValueError("Don't run on openshift or Kubernetes")


def main():
    #t1 = threading.Thread(target=watch_nodes, args=("WatchNodes", "Node"), daemon=True, name='WatchNodes')
    #t1.start()
    #t1.join()
    #t2 = threading.Thread(target=get_nodes, args=("GetNodes", "Node"), daemon=True, name='GetNodes')
    #t2.start()
    #t2.join()
    schedule.every(5).seconds.do(get_nodes, "GetNodes", "Node")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
