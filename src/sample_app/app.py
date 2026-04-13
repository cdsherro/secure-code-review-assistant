import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key"
DEBUG = True

ADMIN_PASSWORD = "admin123"

def run_ping(host):
    cmd = f"ping -n 1 {host}"
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

@app.route("/")
def index():
    return "Secure Code Review Assistant project test app"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if username == "admin" and password == ADMIN_PASSWORD:
        return "login success"
    return "login failed"

@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    return str(eval(expr))

@app.route("/search")
def search():
    term = request.args.get("term", "")
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{term}'"
    rows = cur.execute(query).fetchall()
    conn.close()
    return {"rows": rows}

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    result = run_ping(host)
    return result.stdout

if __name__ == "__main__":
    app.run(debug=DEBUG)
