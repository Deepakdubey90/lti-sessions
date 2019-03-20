# Kubernetes (K8s)

* Portable extensible open source platform for managing containerized workloads
* Container orchestration system for automating application deployment, scaling and management
* Google's [Borg](https://ai.google/research/pubs/pub43438) was open sourced in 2014 as kubernetes
* It's a Greek word meaning helmsman or pilot
* It's also called as K8s (by replacing letters `ubernete` with 8)


# Components

Various binaries required to deliver a functioning K8s cluster

## Master components
* Kube API server
* etcd
* Kube scheduler
* Kube controller manager
* Cloud controller manager

## Worker components
* Kubelet
* Kube proxy
* Container runtime (eg: docker)
