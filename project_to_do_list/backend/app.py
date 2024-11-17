from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)
CORS(app)  # Enable CORS

def get_tasks():
    try:
        conn = psycopg2.connect(
            dbname="todo",
            user="postgres",
            password="postgres",
            host="database"  # Make sure the database service is named 'database' in Kubernetes
        )
        cur = conn.cursor()
        cur.execute("SELECT task FROM tasks")
        tasks = cur.fetchall()
        cur.close()
        conn.close()
        return [task[0] for task in tasks]
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        return []
    except Exception as e:
        print(f"Error fetching tasks: {e}")
        return []

def add_task_to_db(task):
    try:
        conn = psycopg2.connect(
            dbname="todo",
            user="postgres",
            password="postgres",
            host="database"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        cur.close()
        conn.close()
    except OperationalError as e:
        print(f"Database connection failed: {e}")
    except Exception as e:
        print(f"Error adding task: {e}")

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Task API! Use '/tasks' to view all tasks and '/tasks/add' to create new ones."

@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())

@app.route('/tasks/add', methods=['POST'])
def add_task():
    task_data = request.json
    task = task_data.get('task')
    if task:
        add_task_to_db(task)
        return jsonify({'message': 'Task added successfully'}), 201
    return jsonify({'message': 'Task is required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
