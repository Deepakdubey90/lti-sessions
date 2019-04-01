# Pod

* Group of one or more containers
* Basic building block of kubernetes

# Service

* Abstraction which defines a logical set of pods
* Set of pods targeted by a service is usually determined by a LabelSelector

# Ingress

* Expose http and https routes from outside the cluster to the services within the cluster

# ConfigMap

* Binds configuration files and other configuration artifacts to your Pods' containers
* ConfigMaps allow you to separate your configurations from your Pods and components, which helps keep your workloads portable

# Secrets

* Let you store and manage sensitive information such as passwords, tokens, ssh key etc
