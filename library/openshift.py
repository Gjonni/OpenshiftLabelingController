import kubernetes
from openshift.dynamic import DynamicClient
import urllib3
import os
from library.Logging import Logging
from library.rhv import *
from library.ValidationEnviroment import *
import time


kubernetes.config.load_incluster_config()
file_namespace = open("/run/secrets/kubernetes.io/serviceaccount/namespace", "r")
if file_namespace.mode == "r":
    namespace = file_namespace.read()
    print(f"namespace: { namespace }")

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
        if not ValidationEnviroment():
            continue
        host = get_rhv_hosts( node['object'].metadata.name )
        for i in ValidationEnviroment().datacenter:
            if i in host:
                datacenter = i
        Logging.logger.info(f" { ThreadName } - { node['object'].metadata.name } on { host } - {datacenter} ")
        add_label( kind, node["object"].metadata.name, host, datacenter )


def get_nodes(ThreadName,kind):
    v1_ocp = dyn_client.resources.get(api_version="v1", kind=kind)
    nodes_list = v1_ocp.get()
    for node in nodes_list.items:
        host = get_rhv_hosts( node.metadata.name )
        if not ValidationEnviroment():
            continue

        for i in ValidationEnviroment().datacenter:
            if i in host:
                datacenter = i
        Logging.logger.info(f" { ThreadName } - { node.metadata.name } on { host } - { datacenter } ")
        add_label( kind, node.metadata.name, host, datacenter )
