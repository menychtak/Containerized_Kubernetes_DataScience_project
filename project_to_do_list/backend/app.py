from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_tasks():
    conn = psycopg2.connect("dbname=todo user=postgres password=postgres host=database")
    cur = conn.cursor()
    cur.execute("SELECT task FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return [task[0] for task in tasks]

@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify(get_tasks())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)