# Specifications

# System Architecture

![Diagram](/images/diagram.png)

## Components

**Frontend:** JS-based web interface for user interaction (Docker container)

**Backend:** FastAPI-Server with Python as logical controller (Docker container)

**Speech-To-Text:** Whisper (Docker container)

**Translation** Libretranslate (Docker container)

**Text-To-Speech** Tortoise-TTS (Docker container)

**CI/CD Pipeline:** GitHub Actions for automated testing and deployment.

**Monitoring:** AWS CloudWatch and Grafana for metrics, logs, and alerts.

**Backup**: We strictly use repositories for all files. Everything is defined as code. To provide disaster recovery, all repositories are backed up in S3 buckets with cross regional replication.

## Solutions Stack

The project will be deployed to AWS.

Cloud: AWS (EKS, ALB, S3, CloudWatch, Grafana)

Containerization: Docker and Docker Hub

Orchestration: Managed Kubernetes cluster (EKS)

SCM: GitHub

CI/CD: GitHub Actions

Communication: HTTPS, FastAPI

Frontend: JavaScript with websockets

Backend: Python with FastAPI-server

## Interrelationships

## Project (method, breakdown, assignment, planning, ...)

We will use JIRA for the project management. Each task will be assigned to the corresponding team mate. The other team mates will review the tasks and confirm it to the DONE stage.

The 6 epics based on weeks will be defined in JIRA, so that there will be a timeline overview.

## Source code (flow, review, validation,...)

This project will use a workflow inspired by GitFlow.
Our workflow is inspired from here: https://medium.com/@elaurichetoho/optimizing-your-git-workflow-best-practices-for-master-and-develop-branches-472b1738cc06

### Branch structure

`main` branch: The final production stage branch. We will deploy to production from here.

`release` branch: The test stage branch. We will deploy to live testing from here.

`develop` branch: The local developing branch. Used for local development.

`feature` branch: The local developing branch. Used for local development.

### Feature Branches

Naming convention: `feature/feature-name`

Usage: Created from the develop branch for new features or enhancements.

Merging: Merged back into develop when the feature is complete and tested.

### Release Branches

Naming convention: `release/x.x.x`

Usage: Created from develop when preparing for a new release. Allows for minor bug fixes and preparation for release without affecting ongoing development.

Merging: Merged into both master and develop branches when ready for production.

### Hotfix Branches

Naming convention: hotfix/hotfix-name

Usage: Created from master to address critical issues in production.

Merging: Merged into both master and develop to ensure the fix is included in both the production and the next release.

## CI/CD (development cycle stages, jobs, environments)

### GitHub Actions, Docker Hub

This project uses GitHub Actions with workflows with Docker Hub to build the docker images for the K8s cluster.

We will deploy to the staging environment automatically, but deploy to production manually from the console.

## Data (location, replication/distribution, links, access, caching, ...)

### S3

The data will be backed up to S3 buckets with cross regional replication.

## Storage (type - DBMS / Block / File / Object, IOPS, volume, Backup, ...)

### S3

All definitions will be available as code in the GitHub repo. These repos will be backed up to S3 buckets in two regions.

## Network (location, segmentation, addressing, routing, filtering, ...)

### VPC

The project needs a VPC with two availability zones for the EKS cluster, both private and public to access images from Docker Hub.

## Compute (nodes, autoscaling, containers, orchestration,...)

### EKS

We use AWS EKS for easy deployment of the containers and orchestration.

### GPU nodegroups 

There are different nodegroups as we have to use specific GPU nodes for the ML-containers.

### ALB/ELB

A load balancer will direct the incoming traffic to the cluster services.

## Security (AAA, code, traffic, instances, ...)

### IAM roles and policies

One IAM role will be responsible for the deployment and management of the cluster, and each DevOps team mate can assume this role.

## Observability (metrics, logs, traces, alerts)

### Cloudwatch, Grafana, Prometheus

A managed Grafana instance will collect all metrics and send alert in case of errors during the build process, cluster runtime or application error.

## Continuity & Recovery (redundancy, failover, backup, BCP/DRP)

For redundancy it should be possible to point the domains DNS to a load balancer in another region. If the regional datacenter burns down, we could still continue service from another region.
