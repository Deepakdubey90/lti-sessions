# K8s Architecture

![K8s architecture](https://raw.githubusercontent.com/akhilputhiry/lti-sessions/master/kubernetes/k8-architecture.png)

# Controller Manager

* In robotics and automation a control loop is a non terminating loop that regulates the state of the system
* K8 controller watches the state of the cluster via api server
* And makes changes attempting to move the current status towards the desired state
* Examples replication controller, endpoints controller, namespace controller and service account controller

# Scheduler

* Responsible for assigning pod to a node
* Takes care of hardware/software constraints
* Poliy rich, topology aware, workload specific

# Kubelet

* Agent that runs on each node
* Kubelet takes set of PodSpecs and ensures that the containers described in the PodSpec are running and healthy


# Kube Proxy

* Runs on each node
* Responsible for maintaining network rules and performing connection forwarding

# Overlay Network

* Combination of virtual network interfaces, bridges and routing rules is usually called as overlay network
* All hosts has a TUN virtual network kernel interface
* Subnet to host mapping is saved in the etcd
