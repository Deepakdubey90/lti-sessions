# LXC - Linux containers

## What

* LXC is an OS level virtualization technique for tunning multiple isolated linux systems
* LXC was the default execution environment for docker in the early releases, now its been replaced with `libcontainer`

## How

* Linux kernel have something called `cgroups` and `namespace isolation`
    * cgroups allows limitation and prioritation of resources for a collection of resources
    * namespace isolation partitions the kernel resources, so that one set of processes see one set of resources while other set of processes see other set of resources
    
    
