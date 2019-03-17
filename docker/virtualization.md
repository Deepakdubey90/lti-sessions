# Virtualization

## What

* Masking server resources from users
* Divide physical server into multiple virtual environments/servers
* These virtual environments are often referred to as guests, instances, emulation, container etc

## Popular approaches

* Virtual machine model
    * Relies on software to simulate the hardware functionality - hypervisor
    * Two types of hypervisors - bare metal and hosted
* Para virtual machine
    * Allows to have an interface that can differ from underlying hardware
    * OS should be compiled specifically from the hypervisor
* OS level virtualization [Container based virtualization]
    * Operating system is modified to operate as multiple independent systems

## How container virtualization works

* Linux kernel have something called `cgroups` and `namespace isolation`
* cgroups allows limitation and prioritation of resources for a collection of resources
* namespace isolation partitions the kernel resources, so that one set of processes see one set of resources while other set of processes see other set of resources
* combining these cgroups and namespace isolation container virutalization was implemented
* The set of tools used to perform container virtualization is called LXC, LXD, LXCFS etc
