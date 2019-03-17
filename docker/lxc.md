# Open Container Initiative - OCI

## Why

* There are many technologies out there eg: LXC, CRI-O, Containerd, runc etc
* These systems were not interoperable or standardised
* In 2015 Docker, Google and CoreOS created open container initiative
* The specification can be found [here](https://github.com/opencontainers/runtime-spec)

## How

* Linux kernel have something called `cgroups` and `namespace isolation`
    * cgroups allows limitation and prioritation of resources for a collection of resources
    * namespace isolation partitions the kernel resources, so that one set of processes see one set of resources while other set of processes see other set of resources
    
    
