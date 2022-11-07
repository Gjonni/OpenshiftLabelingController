SHELL=/bin/bash
### SOLO TESTING NON SO SE FUNGE

NAMESPACE = gfilice-test
NAME = rhv-label
TZ = Europe/Rome
ENGINE_URL = ""
##ENGINE_URL = ""
USERNAME = ''
PASSWORD = ''
LOGLEVEL = INFO
DATACENTER = 'datacenter1,datacenter2'

install:
	@echo "Creazione Project"
	oc new-project $(NAMESPACE)
	@echo "Creazione Applicazione"
	oc new-app openshift/python:3.9-ubi8~https://github.com/Gjonni/ocp-label-node.git --name=$(NAME) -n $(NAMESPACE)
	oc create  sa $(NAME) -n $(NAMESPACE)
	oc label sa $(NAME) app=$(NAME) -n $(NAMESPACE)
	@echo "Add Secrets"
	oc create secret generic rhv-credential --from-literal ENGINE_URL=$(ENGINE_URL) --from-literal USERNAME=$(USERNAME)  --from-literal PASSWORD=$(PASSWORD)
	@echo "Add Enviroment"
	oc patch deployment $(NAME) -p '{"spec":{"template":{"spec":{"serviceAccount": "$(NAME)" }}}}' -n $(NAMESPACE)
	oc set env deployment/$(NAME) TZ=$(TZ) LOGLEVEL=$(LOGLEVEL) -n $(NAMESPACE)
	oc set env --from=secret/rhv-credential deployment/$(NAME)
	oc scale deployment/$(NAME) --replicas=1 -n $(NAMESPACE)
	@echo "Fix Permission"
	oc adm policy add-cluster-role-to-user cluster-admin system:serviceaccount:$(NAMESPACE):$(NAME) -n $(NAMESPACE)



uninstall:
	@echo "Disinstallo Applicazione"
	oc delete all --selector app=$(NAME) -n $(NAMESPACE)
	oc adm policy remove-cluster-role-from-user cluster-admin system:serviceaccount:$(NAMESPACE):$(NAME) -n $(NAMESPACE)
	oc delete sa $(NAME) -n $(NAMESPACE)
	oc delete project $(NAMESPACE)
