import kubernetes
from openshift.dynamic import DynamicClient
import urllib3
import os
from library.Logging import Logging
from library.rhv import *
import time

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


def add_label(kind, name, host, datacenter):
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




def watch_nodes(ThreadName,kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    for node in v1_ocp.watch():
        host = get_rhv_hosts( node['object'].metadata.name )
        if "bernina" in host:
            datacenter = "Bernina"
        if "caracciolo" in host:
            datacenter = "Caraccialo"     
        Logging.logger.debug(f"{ node['object'].metadata.name } on { host } - {datacenter} ")
        add_label( kind, node["object"].metadata.name, host, datacenter )


def get_nodes(ThreadName,kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    nodes_list = v1_ocp.get()
    for node in nodes_list.items:
        host = get_rhv_hosts( node.metadata.name )
        if "bernina" in host:
            datacenter = "Bernina"
        if "caracciolo" in host:
            datacenter = "Caraccialo"
        Logging.logger.debug(f"{ node.metadata.name } on { host } - { datacenter } ")
        add_label( kind, node.metadata.name, host, datacenter )
    while True:
        Logging.logger.debug(f"Verifica ogni 10 secondi completata correttamente")
        time.sleep(10)



