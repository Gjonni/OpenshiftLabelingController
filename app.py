import os
import _thread
from library.Logging import *
from library.openshift import *
import sched
import time


def main():
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(3, 1, watch_nodes, ("WatchNodes", "Node"))
    scheduler.enter(3, 1, get_nodes, ("GetNodes", "Node"))
    scheduler.run()
#    Logging.logger.info(f"Inizio la verifica degli host fisici di RHV su sui si trovano i nodi Openshift")
#    _thread.start_new_thread(watch_nodes, ("WatchNodes", 2, "Node"))


if __name__ == "__main__":
    main()


