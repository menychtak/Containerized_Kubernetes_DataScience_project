from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Task API!"

@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)