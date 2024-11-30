
# Containerized Kubernetes Data Science Project

This project is a containerized application built with Flask for managing a simple to-do list, integrated with a PostgreSQL database. It is designed to run with Docker containers and includes a frontend interface to interact with the backend. Additionally, it can be deployed using Kubernetes for orchestration and management of the services.

## Features

- Add tasks to a to-do list
- View existing tasks
- Simple frontend to interact with the backend
- PostgreSQL integration for persistent storage
- Containerized using Docker
- Kubernetes support for deployment

## Prerequisites

- Docker installed
- `docker-compose` installed
- Kubernetes (`kubectl`) installed
- Minikube installed
- Git installed

## Project Structure

```
├── project-to-do-list/       # Main project directory
│   ├── backend/              # Backend application files
│   │   ├── Dockerfile        # Dockerfile for the Flask app
│   │   ├── app.py            # Flask backend application
│   │   └── requirements.txt  # Python dependencies for the backend
│   ├── database/             # Database configuration files
│   │   ├── Dockerfile        # Dockerfile for the PostgreSQL database
│   │   └── init.sql          # SQL script to initialize the database
│   ├── frontend/             # Frontend application files
│   │   ├── Dockerfile        # Dockerfile for the frontend
│   │   ├── html/             # Directory containing HTML files
│   │   └── index.html        # Main HTML file for the frontend
│   ├── k8s/                  # Kubernetes configuration files
│   │   ├── deployment.yaml   # Deployment configuration for Kubernetes
│   │   └── service.yaml      # Service configuration for Kubernetes
├── README.md                 # Project documentation
└── docker-compose.yml        # Docker Compose configuration file
```

## Getting Started

### 1. Clone the Repository

```bash
sudo git clone https://github.com/menychtak/Containerized_Kubernetes_DataScience_project
cd Containerized_Kubernetes_DataScience_project
```

### Running with Docker and Docker Compose

### 2. Build network (docker-net)

```bash
sudo docker network create docker_net
```

### 3. Run the Application

Use Docker Compose to run the entire stack (frontend, backend, database):

```bash
sudo docker-compose up --build -d
```

### 4. Access the Application

- Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).
- The frontend interface allows you to add new tasks and view existing ones.

You can go into view mode or add tasks mode by visiting [http://localhost:5000/tasks](http://localhost:5000/tasks) and [http://localhost:5000/tasks/add](http://localhost:5000/tasks/add) accordingly.

### 5. Available Endpoints

- `GET /tasks` - View all tasks
- `POST /tasks/add` - Add a new task

To add a task using `curl`:

```bash
curl -X POST http://localhost:5000/tasks/add -H "Content-Type: application/json" -d '{"task": "Learn Kubernetes"}'
```

### 6. Cleaning Up

To stop and remove the containers, run:

```bash
sudo docker-compose down
```

To remove the project directory:

```bash
sudo rm -rf Containerized_Kubernetes_DataScience_project
```

## Kubernetes Deployment Steps

### 1. Install kubectl

```bash
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo mv ./kubectl /usr/local/bin/kubectl
sudo chmod +x /usr/local/bin/kubectl
kubectl version --client
```

### 2. Install Minikube

```bash
cd ~
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
sudo chmod +x /usr/local/bin/minikube
minikube start
```

### 3. Verify Cluster Setup

```bash
kubectl cluster-info
kubectl get nodes
```

### 4. Deploy to Kubernetes

```bash
cd ~/Downloads/Containerized_Kubernetes_DataScience_project/project_to_do_list/k8s
kubectl apply -f .
kubectl get pods
kubectl get services
```

### 5. Accessing the Application

- Get the Minikube IP:

  ```bash
  minikube ip
  ```
  - Get the NodePort:

  ```bash
  kubectl get svc
  ```

- Use the Minikube IP and the NodePort of the frontend service to access the application:

  ```
  http://<Minikube-IP>:<NodePort>
  ```
### 6. Stop Cluster

```bash
minikube stop
```

Optinal step to completely delete Cluster
```bash
minikube delete
```
---
