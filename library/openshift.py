import kubernetes
from openshift.dynamic import DynamicClient
import urllib3
import os
import _thread
from library.Logging import Logging
from library.rhv import *



urllib3.disable_warnings()
if "OPENSHIFT_BUILD_NAME" in os.environ:
    kubernetes.config.load_incluster_config()
    file_namespace = open("/run/secrets/kubernetes.io/serviceaccount/namespace", "r")
    if file_namespace.mode == "r":
        namespace = file_namespace.read()
        print(f"namespace: { namespace }")
else:
    kubernetes.config.load_kube_config()


k8s_client = kubernetes.client.ApiClient()
dyn_client = DynamicClient(k8s_client)

def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def label(kind, name, host):
    resources = dyn_client.resources.get(api_version="v1", kind=kind)
    body = {
        "kind": kind,
        "apiVersion": "v1",
        "metadata": {
            "name": name,
            "labels":{ "rhv": host},
            },
    }
    Logging.logger.debug(f"{ name } - { host } ")
    resources.patch(body=body)




def watch_nodes(ThreadName, delay, kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    for node in v1_ocp.watch():
        Logging.logger.info(f"{ThreadName } -  { node['object'].metadata.name } on { get_hosts(node['object'].metadata.name) } ")
        label( kind, node["object"].metadata.name, get_hosts(node["object"].metadata.name) )


def get_nodes(ThreadName, delay, kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    nodes_list = v1_ocp.get()

    for node in nodes_list.items:
        print(project.metadata.name)
        Logging.logger.info(f"{ThreadName } -  { node['object'].metadata.name } on { get_hosts(node['object'].metadata.name) } ")
        label( kind, node.metadata.name, get_hosts(node.metadata.name) )



