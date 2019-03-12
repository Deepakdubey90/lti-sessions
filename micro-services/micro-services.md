# Micro Services

* Approach to developing a single application as a suite of small services
* Each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API
* These services are built around business capabilities and independently deployable by fully automated deployment machinery

## What problems does it solve

* Smaller codebases - developer efficiency
* Availability and Scalability
* Easy less risky deployments
* Runtime resiliency
* Polyglotic programming / Application lifecycle flexibility

## What happened later

* Serverless - Function as a service
* Unikernels

## Operational challenges and work arounds

* Sharing data between microservices
* API versioning
* Transactions become pain in the a**
* Network latency
