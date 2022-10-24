# Rolling Deployment Kubernetes Lab

### Introduction

- In this lab, you will be creating a pipeline that does a canary deployment of a Kubernetes Application
- You will learn how Harness performs the deployment and process each step before deployment
- In case of failure, you will learn how to navigate the logs to see what went wrong in the console view

### Pre-Requisistes

- Kubernetes Cluster
- Harness Delegate
- Github Connector to fetch the Manifests
- Docker Connector to fetch the artifact image tag
- Have a project in Harness with admin access to it



### Lab 

1. Make sure all the connectors, the delegate and the target infrastructure are all set before proceeding with this lab
2. Create a Pipeline
3. Add a Deploy Stage
4. Select a Kubernetes Deployment Type for the stage
5. Configure a K8s Service - call it nginx
6. Within the service configure the nginx K8s manifests from github
7. Within the service configure the artifact to be the docker image `library/nginx` in th artfiact section of the service
8. Navigate to Infrastructure by clicking continue. Configure the Environment and call it dev as well as the infrastrxutrue definition for the Kubernetes cluster
9. Click Continue, and navigate to execution and pick the canary execution strategy - Please Read the animation - itll help with the questions



### Questions

1. What does Harness do in the Canary Deployment and Canary Delete Steps of the deployment? How is the application being orchestrated?
2. Can you find the taskID for the Canary Deployment Step?
3. What were the step outputs of the canary depeloyment step? 






