import ovirtsdk4 as sdk
import os

connection = sdk.Connection(
    url= os.environ.get("ENGINE_URL"),
    username= os.environ.get("USERNAME"),
    password= os.environ.get("PASSWORD")
    insecure=True,
    debug=False
)


def get_hosts(vmname):
    vms_service = connection.system_service().vms_service()
    for vm in vms_service.list():
        if vm.name == vmname:
            host = connection.follow_link(vm.host)
            return host.name        
    connection.close()

