# Service Oriented Architecture (SOA)

* Collection of services
* Where service is a discrete unit of functionality
    * self contained
    * represents business activity
    * black box for consumers
* SOA was started with the idea, `do the simplest thing that could possibly work`
* The first implementation of SOA was Simple Object Access Protocol (SOAP) by Microsoft in 1999
* It quickly established since it could easily iteroperate with systems build in different languages
    
## What problems does it solve

* Interoperability

## What happened later

* People started adding more layers beyond simple method invokation
* Extra layers were added for
    * Exception handling
    * Transaction support
    * Security and digital signatures
* Then all of a sudden it became a complicated protocol
* This led to the observation

```
Trying to make a distributed call act like 
a local call always ends in tears
```
