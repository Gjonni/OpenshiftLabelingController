import os
from library.Logging import *
from library.openshift import *
import schedule
import threading


#if "OPENSHIFT_BUILD_NAME" in os.environ:
#    from library.openshift import *
#else:
#    raise ValueError("Don't run on openshift or Kubernetes")

def run_threaded(job,kind):
    job_thread = threading.Thread(target=job, args=("Get"+kind, kind), daemon=True)
    job_thread.start()
    job_thread.join()

def main():
    schedule.every(5).seconds.do(run_threaded, get_nodes, "Node")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
