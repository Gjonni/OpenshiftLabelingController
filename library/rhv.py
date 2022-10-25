import ovirtsdk4 as sdk
import os
from library.ValidationEnviroment import *

connection = sdk.Connection(
    url = ValidationEnviroment().engineUrl,
    username = ValidationEnviroment().username,
    password = ValidationEnviroment().password,
    insecure = True,
    debug = False
)


def get_rhv_hosts(vmname):
    vms_service = connection.system_service().vms_service()
    for vm in vms_service.list():
        if vm.name == vmname:
            host = connection.follow_link(vm.host)
            return host.name        
    connection.close()

