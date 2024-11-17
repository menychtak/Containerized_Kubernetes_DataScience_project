from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to connect and get tasks
def get_tasks():
    try:
        conn = psycopg2.connect(
            dbname="todo",
            user="postgres",
            password="postgres",
            host="database"
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

# Function to add a task to the database
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

@app.route('/tasks/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Handle POST request to add a task
        if request.is_json:
            task_data = request.json
            task = task_data.get('task')
        else:
            task = request.form.get('task')  # Handle form submissions as well
        
        if task:
            add_task_to_db(task)
            return jsonify({'message': 'Task added successfully'}), 201
        return jsonify({'message': 'Task is required'}), 400

    # Handle GET request to show a form in the browser
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Add Task</title>
    </head>
    <body>
        <h1>Add a New Task</h1>
        <form action="/tasks/add" method="POST">
            <label for="task">Task:</label><br>
            <input type="text" id="task" name="task"><br><br>
            <input type="submit" value="Add Task">
        </form>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
