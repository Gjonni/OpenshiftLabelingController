import os
import threading
from library.Logging import *
from library.openshift import *
import sched
import time


def worker():
    scheduler.enter(3, 1, watch_nodes, ("WatchNodes", "Node"))
    scheduler.enter(3, 1, get_nodes, ("GetNodes", "Node"))
    scheduler.run
    print(scheduler.queue)

def main():
    t = threading.Thread(target=worker, args=())
    t.start()
#    Logging.logger.info(f"Inizio la verifica degli host fisici di RHV su sui si trovano i nodi Openshift")
#    _thread.start_new_thread(watch_nodes, ("WatchNodes", 2, "Node"))


if __name__ == "__main__":
    scheduler = sched.scheduler(time.time, time.sleep)
    main()


