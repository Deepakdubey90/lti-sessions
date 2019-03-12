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
* Industry slowly started to reject procedural, layered concepts inherent in SOAP and WS-* standards
* Then the concept of [representation state transfer (REST)](https://github.com/akhilputhiry/lti-sessions/blob/master/micro-services/rest.md) was introduced
* At the same time, the industry was also moving to reject another legacy of the Java Platform,
    * Enterprise Edition (JEE) and 
    * SOA world: the large farm of application servers
* Developers preferred were smaller, light weight application platforms
* The complexity of JEE was being shunned in favor of the supposed simplicity of the Spring platform as techniques like 
    * Inversion of Control and 
    * Dependency Injection became common
* This led to the other observation
```
Whenever possible, your programs and their runtime environments should be entirely self-contained.
```
