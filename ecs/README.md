# ECS Introduction

AWS provides a service called Elastic Container Services, which allows developers to run their containerized application on VMs or through a Fargate configuration.

## ECS Basics
Amazon Elastic Container Services is a highly scalable, fast, contianer management service that makes it easy to run, stop and manage docker containers on a cluster. We can host the cluster on serverless infrastructure using Fargate.

An ECS cluster is a cluster of EC2 instances. Each EC2 instance has a: VPC, subnet and security group. Each instance can have one VPC, multiple subnets, and up to 5 security groups. You pick how many nodes add an Auto Scaling Group. When you add an instance through EC2, a user has to wait for the VM to come up, install ECS and have it become part of the cluster.

An ECS cluster configured through Fargate, doesn’t allow the user to control the underlying infrastructure.

ECS lets you start and stop container based applications through API calls. It also allows you to operate and manage your cluster without having to worry about scaling the infrastructure and managing the configuration.

However, in order to run in ECS, the application must be containerized and must be pulled from some sort of registry.

## ECS Terminology

Task Definition: This a blueprint that describes how a docker container should launch. If you are already familiar with AWS, it is like a LaunchConfig except instead it is for a docker container instead of a instance. It contains settings like exposed port, docker image, cpu shares, memory requirement, command to run and environmental variables.

Task: This is a running container with the settings defined in the Task Definition. It can be thought of as an “instance” of a Task Definition.

Service: Provides scheduling, load balancing, and discovery capabilities for long running tasks as well as ensuring the desired number of tasks are running. This can be 1 running container or multiple running containers all using the same Task Definition.

Cluster: A logic group of EC2 instances. When an instance launches the ecs-agent software on the server registers the instance to an ECS Cluster. This is easily configurable by setting the ECS_CLUSTER variable in /etc/ecs/ecs.config described here: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html.

Container Instance: This is just an EC2 instance that is part of an ECS Cluster and has docker and the ecs-agent running on it.

