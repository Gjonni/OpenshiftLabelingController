import kubernetes
from openshift.dynamic import DynamicClient
import urllib3
import os
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


def label(kind, name, host, datacenter):
    resources = dyn_client.resources.get(api_version="v1", kind=kind)
    body = {
        "kind": kind,
        "apiVersion": "v1",
        "metadata": {
            "name": name,
            "labels":{ "rhv": host, "datacenter": datacenter},
            },
    }
    Logging.logger.debug(f"{ name } - { host } ")
    resources.patch(body=body)




def watch_nodes(ThreadName, delay, kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    for node in v1_ocp.watch():
        host = get_hosts(node.metadata.name)
        Logging.logger.debug(f"{ ThreadName } -  { node['object'].metadata.name } on { get_hosts(node['object'].metadata.name) } ")
        if "bernina" in get_hosts(node.metadata.name):
            datacenter = "Bernina"
        if "caracciolo" in get_hosts(node.metadata.name):
            datacenter = "Caraccialo"       
        label( kind, node["object"].metadata.name, host, datacenter )
    Logging.logger.debug(f"Ogni nodo è stato correttamente identificato e ho aggiunto la label rhv=nodo fisico")


def get_nodes(ThreadName, delay, kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    nodes_list = v1_ocp.get()
    for node in nodes_list.items:
        host = get_hosts(node.metadata.name)
        Logging.logger.debug(f"{ThreadName } -  { node.metadata.name } on { host } ")
        if "bernina" in get_hosts(node.metadata.name):
            datacenter = "Bernina"
        if "caracciolo" in get_hosts(node.metadata.name):
            datacenter = "Caraccialo"
        label( kind, node.metadata.name, host, datacenter )
    Logging.logger.debug(f"Ogni nodo è stato correttamente identificato e ho aggiunto la label rhv=nodo fisico")



