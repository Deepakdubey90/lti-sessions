# Remote Procedure Calls (RPC)

* RPC concept was introduced to the world by ONC RPC, DCE and CORBA architectures in 1988 - 1990
* When a program causes a routine,
  * To execute in a different address space
  * As if it was a local call
  * Without explicitly coding the details of remote interaction

## What problems does it solve

* Enabled developers to build larger machine crossing systems
* Could avoid processing and memory scalability issues that affected systems of that time
* In 1990s the CPUs where of 16 bit and 64K address space

## What happened later

* As the processors and address spaces evolved, this issue became less important
* Large implementations of RPCs taught an important observation to the architects regarding distributed computing

```
Just because something can be distributed 
doen't mean it should be distributed
```
* Poor choices about distributing the methods across machines started impacting system performance
* Networking overhead vastly outweighted the advantages of distibution (Think about the network speed in 1990s)
