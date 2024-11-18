
# Containerized Kubernetes Data Science Project

This project is a containerized application built with Flask for managing a simple to-do list, integrated with a PostgreSQL database. It is designed to run with Docker containers and includes a frontend interface to interact with the backend.

## Features

- Add tasks to a to-do list
- View existing tasks
- Simple frontend to interact with the backend
- PostgreSQL integration for persistent storage
- Containerized using Docker

## Prerequisites

- Docker installed
- `docker-compose` installed
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
└── docker-compose.yml        # Project documentation
```

## Getting Started

### 1. Clone the Repository

```bash
sudo git clone https://github.com/menychtak/Containerized_Kubernetes_DataScience_project
cd Containerized_Kubernetes_DataScience_project
```

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

You can got into view mode or add tasks mode by [http://localhost:5000/tasks](http://localhost:5000/tasks) and [http://localhost:5000/tasks/add](http://localhost:5000/tasks/add) accordingly.

### 5. Available Endpoints

- `GET /tasks` - View all tasks
- `POST /tasks/add` - Add a new task

To add a task using `curl`:

```bash
curl -X POST http://localhost:5000/tasks/add -H "Content-Type: application/json" -d '{"task": "Learn Kubernetes"}'
```

### 7. Cleaning Up

To stop and remove the containers, run:

```bash
sudo docker-compose down
```

To remove the project directory:

```bash
sudo rm -rf Containerized_Kubernetes_DataScience_project
```

## Notes

This project is licensed under the MIT License. See the LICENSE file for details.
