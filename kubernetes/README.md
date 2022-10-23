# Kubernetes Training Guide for Harness

## Introduction

The intention of this training is to help Harness teammates get familiar with Kubernetes and Harness CD. Once completing the exercise, you should be comfortable to configure, troubleshoot and help customers onboard, adopt Harness and learn about new feauters in the Harness CD Prduct. Each training will come with a lab that should be completed before proceeding to the next swimlane or technology. 

## Kubernetes High Level


Kubernetes is an open-source, highly scalable, portable, and extensive container orchestration system. It was originally based on Google’s Borg project and has been rewritten in Go and has been open-sourced to the community. It has been widely adopted and is gaining traction in the enterprise space.
However, Kubernetes is not a PaaS (Platform as a Service). In the field, many developers do make that confusion. Kubernetes is a tool that empowers developers to build their own custom PaaS for their specific use cases.


### Kubernetes Key Concepts

In Kubernetes, we have various concepts, such as pods, service, deployment, ingress, etc. These concepts can be complicated and confusing when you start mixing them all together. In this section, we will break it down to the core ones that we encounter in the field with our customers.
When you utilize the Kubernetes command line,

Pod

The basic definition of a pod - " a unit of deployment or work" in Kubernetes terminology. This pod represents a process in the cluster. Pods can run a single docker container inside of it or can run multiple Docker containers all talking together. It’s mostly user preference which way a pod is created in Kubernetes.

For further reading: What is a Pod?

Service

A service is a way to expose an application running on a group of pods. There are a few types of Services, there is the ClusterIP, LoadBalancer, and NodePort.
Definitions for each:
ClusterIP: Exposes the service on a cluster-internal IP. Choosing this value makes the service only reachable from within the cluster. This is the default ServiceType

NodePort: Exposes the service on each Node’s IP at a static port (the NodePort). A ClusterIP service, to which the NodePort service will route, is automatically created. You’ll be able to contact the NodePort service, from outside the cluster, by requesting `<NodeIP>:<NodePort>`.

LoadBalancer: Exposes the service externally using a cloud provider’s load balancer. NodePort and ClusterIP services, to which the external load balancer will route, are automatically created.

Stackoverflow provides an excellent summary on this:

A ClusterIP exposes the following:

`spec.clusterIp:spec.ports[].port`
You can only access this service while inside the cluster. It is accessible from its `spec.clusterIP port`. If a `spec.ports[].targetPort` is set it will route from the port to the targetPort. The CLUSTER-IP you get when calling kubectl get services is the IP assigned to this service within the cluster internally.

A NodePort exposes the following:
```
<NodeIP>:spec.ports[*].nodePort
spec.clusterIp:spec.ports[*].port
```

If you access this service on a nodePort from the node’s external IP, it will route the request to

`spec.clusterIp:spec.ports[*].port`, which will in turn route it to your `spec.ports[*].targetPort`, if set. This service can also be accessed in the same way as ClusterIP.
Your NodeIPs are the external IP addresses of the nodes. You cannot access your service from 
```
<ClusterIP>:spec.ports[*].nodePort.
```

A **LoadBalancer** exposes the following:

```
spec.loadBalancerIp:spec.ports[*].port
<NodeIP>:spec.ports[*].nodePort
spec.clusterIp:spec.ports[*].port
```
You can access this service from your load balancer's IP address, which routes your request to a nodePort, which in turn routes the request to the clusterIP port. You can access this service as you would a NodePort or a ClusterIP service as well.

For Further Reading:
[What is a Service?](https://kubernetes.io/docs/concepts/services-networking/service/)
[Services in Detail](https://stackoverflow.com/questions/41509439/whats-the-difference-between-clusterip-nodeport-and-loadbalancer-service-types)

#### Deployment
A Deployment creates pods and services. You see the deployment and what it contains in the deployment.yaml file. You can control the states of the pods and replica sets with deployments. If the desired state is different from the current state, a user can update the YAML and apply the new deployment YAML in Kubernetes. Kubernetes will make the specified adjustments to match the desired state.
For Further Reading: [What is a Deployment?](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

#### Volumes
In Kubernetes, there are various types of storage configurations a user can specify. A volume is the basic storage configuration for a pod. If containers are running in a pod and sharing files or data, that data is generally stored in a volume. However, if the pod were to be killed or destroyed the data that the volume contained would also be gone.
For Further Reading: What are Volumes?
Note: Docker Volumes are different from Kubernetes volumes

#### Persistent Volumes
This is a relatively new concept in Kubernetes however, many organizations do want their data to persist. If a pod were to die and be spun back up due to Kubernetes' self-healing capabilities, they would like their data to remain and still be available for consumption. This is where Persistent Volumes come in. They are storage that is provisioned in the cluster by an administrator. They are Kubernetes Storage Class plugins they have an independent life cycle from the pod.
Every Persistent Volume has a Persistent Volume Claim, which is written in YAML to tell Kubernetes this is how many resources my volume is going to need.
Example: Portworx, centOS, Amazon EBS.
For Further Reading: What are Persistent Volumes?

#### ConfigMap

Keeps the configuration information separate from the application image. As a result, both the configuration and application are portable and can be leveraged in different Kubernetes environments.
For Further Reading: What are ConfigMaps?
Secrets
Kubernetes has the object of a secret that lets the user store sensitive information, such as a password, token or a private key. It is a much more secure way than storing the information in the application.

Harness also supports HashiCorp's Vault Secrets Management tool. It's designed to make sure that secrets remain secret for Kubernetes.

For Further Reading: What are Secrets?

#### Ingress
Ingress allows a user to access their pod or service outside the cluster. It generally exposes a port on the cluster to allow outside traffic in.

Diagram:

```
internet
    |
[ Ingress ]
–|-----|–
[ Services ]
```

There must be an ingress controller in order to utilize ingress.
For Further Reading: What is Ingress?
Replication Controller
Replication Controllers is a Kubernetes object that defines a pod template. It controls the number of identical pods to increase or decrease in scale horizontally. This is an easy way to distribute the load and increase availability natively within Kubernetes.

From DigitalOcean:
The replication controller is responsible for ensuring that the number of pods deployed in the cluster matches the number of pods in its configuration. If a pod or underlying host fails, the controller will start new pods to compensate. If the number of replicas in a controller's configuration changes, the controller either starts up or kills containers to match the desired number. Replication controllers can also perform rolling updates to roll over a set of pods to a new version one by one, minimizing the impact on application availability.

#### Daemonsets
Daemonsets ensure that all nodes are running a copy of a pod. As nodes are added to a cluster the pod will be copied to the new node. When nodes are deleted the daemonset will also be deleted and the pod will be deleted as well.
For Further Reading on Daemonsets: [What are Daeomonsets?](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)

#### RepicaSets
Defines the set of pods that should be running at all times. It is often used to guarantee the availability of identical pods. ReplicaSets use pod templates to create new pods with identical attributes. They are the iteration on top of the replica controller and with greater flexibility in how the controller identifies the pods it is meant to manage. They are beginning to replace replication controllers in certain scenarios. ReplicaSets can't do rolling updates to cycle backends as replication controllers can.
For Further Reading: [What are ReplicaSets?](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)

#### RBAC

Role-Based Access Control

This is an important security concept for Kubernetes. By default, Kubernetes is a deny by default system. Meaning, a user won't have access to utilize or interact with any of the resources without having an RBAC configuration set up by the Cluster admin. RBAC prevents users from getting unnecessary access to specific portions of the Kubernetes cluster.
RBAC dictates what specific resources and commands the user can use while in the cluster. The more fine-grained the better for security.
For Further Reading on RBAC: [What is RBAC?](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

#### Namespace
In order to organize the Kubernetes cluster for various team uses, namespaces are created to segment the various teams' workloads. Namespaces are virtual clusters within the main Kubernetes cluster. Each namespace can be given specific resource constraints, can be locked down for only specific team members. It's an excellent way to have 1 cluster and multiple teams leveraging it.
For Further Reading: [What is a Namespace?](http://kubernetesbyexample.com/ns/)

#### Other Resources
- [Kubernetes Core Concepts, Medium Blog](https://medium.com/yld-blog/kubernetes-core-concepts-324ea7028c29)

- [Kubernetes Core Concepts from Kubernetes](https://kubernetes.io/docs/concepts/)

- [Harness Overview of K8s Deployments](https://docs.harness.io/article/pc6qglyp5h-kubernetes-deployments-overview)

- [DigitalOcean's Blog on Kubernetes](https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes)

- [Service Mesh Reading](https://www.redhat.com/en/topics/microservices/what-is-a-service-mesh)

#### Tutorials on Kubernetes
[K8s Tutorial, Configuring, running and managing](https://www.tutorialspoint.com/kubernetes/index.htm)

#### Harness Reading
[Harness Presentation on K8s](https://docs.google.com/presentation/d/1Z591sYLofUF31LuV0MelcrEQudGTVOlPNGxu4X0fMG8/edit#slide=id.p1)
