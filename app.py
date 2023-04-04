import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10tsdb_user:6agfPU8lS9HEoX1PefNWXxgdkREINjJc@dpg-cglpdthmbg56g47s7920-a/lab10tsdb")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10tsdb_user:6agfPU8lS9HEoX1PefNWXxgdkREINjJc@dpg-cglpdthmbg56g47s7920-a/lab10tsdb")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"