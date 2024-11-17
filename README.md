# Containerized Kubernetes Data Science Project

This project is a containerized application built with Flask for managing a simple to-do list, integrated with a PostgreSQL database. It is designed to run in a Kubernetes environment with Docker containers.

## Features

- Add tasks to a to-do list
- View existing tasks
- Simple frontend to interact with the backend
- PostgreSQL integration for persistent storage
- Containerized using Docker
- Configured to run on Kubernetes

## Prerequisites

- Docker installed
- Kubernetes (Minikube or any other Kubernetes cluster)
- `kubectl` command-line tool
- PostgreSQL client (optional, for database interaction)

## Project Structure

```
.
├── app.py                # Flask backend application
├── Dockerfile            # Dockerfile for the Flask app
├── index.html            # Frontend for interacting with the task list
├── requirements.txt      # Python dependencies
├── k8s/                  # Kubernetes configuration files
│   ├── deployment.yaml   # Deployment for the Flask app and PostgreSQL
│   └── service.yaml      # Service configuration for the Flask app
└── README.md             # Project documentation
```

## Getting Started

### 1. Build Docker Images

Build the Docker image for the Flask application:

```bash
docker build -t flask-todo-app .
```

### 2. Deploy to Kubernetes

Apply the Kubernetes configurations:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 3. Access the Application

Forward the service port to your local machine (if necessary):

```bash
kubectl port-forward svc/flask-service 5000:5000
```

Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

### 4. Available Endpoints

- `GET /tasks` - View all tasks
- `POST /tasks/add` - Add a new task

### 5. Frontend Interaction

The frontend interface is accessible via the root URL and allows you to add new tasks using a form and view existing tasks.

## Environment Variables

The following environment variables can be configured:

- `DB_NAME` - Name of the PostgreSQL database
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password
- `DB_HOST` - Hostname of the database (use `database` when running in Kubernetes)

## Notes

- Ensure that the database connection is correctly configured in `app.py`.
- This project assumes a running PostgreSQL instance with a `tasks` table.
- Kubernetes configurations can be adjusted as needed to match your cluster's requirements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
