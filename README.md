# OpenshiftLabelingController


# Docker Pull
docker pull harbor.k3s.filice.eu/library/openshiftlabelingcontroller@sha256:8f7518ce103ed52e0baaa4ec2122ceef4c7add345cb7afe7eacbdef845cc6bf6
docker pull harbor.k3s.filice.eu/library/openshiftlabelingcontroller:latest

**Variabili d'ambiente**

|Variabile      |Esempio                  |Descrizione                                                                   |
|---------------|-------------------------|------------------------------------------------------------------------------|
|TZ             |Europe/Rome              |Impostare il timezone del micro\-servizio                                     |
|NAMESPACES     |test\-namespace          |Impostare una lista i namespaces da tenere sotto controllo                    |
|LOGLEVEL       |INFO                     |Impostare il livello di verbosità                                             |
|ENGINE_URL     |https://xx.xx.xx.xx//ovirt-engine/api| Ovirt api engine                                                 |
