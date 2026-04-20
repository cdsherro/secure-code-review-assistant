Review this Python web app for security issues. List the findings, explain why each one matters, and suggest a fix.



import sqlite3

import subprocess

from flask import Flask, request



app = Flask(\_\_name\_\_)

app.config\["SECRET\_KEY"] = "dev-secret-key"

DEBUG = True



ADMIN\_PASSWORD = "admin123"





def run\_ping(host):

&#x20;   cmd = f"ping -n 1 {host}"

&#x20;   return subprocess.run(cmd, shell=True, capture\_output=True, text=True)



@app.route("/")

def index():

&#x20;   return "Secure Code Review Assistant project test app"



@app.route("/login", methods=\["POST"])

def login():

&#x20;   username = request.form.get("username", "")

&#x20;   password = request.form.get("password", "")

&#x20;   if username == "admin" and password == ADMIN\_PASSWORD:

&#x20;       return "login success"

&#x20;   return "login failed"



@app.route("/calc")

def calc():

&#x20;   expr = request.args.get("expr", "1+1")

&#x20;   return str(eval(expr))



@app.route("/search")

def search():

&#x20;   term = request.args.get("term", "")

&#x20;   conn = sqlite3.connect("example.db")

&#x20;   cur = conn.cursor()

&#x20;   query = f"SELECT \* FROM users WHERE name = '{term}'"

&#x20;   rows = cur.execute(query).fetchall()

&#x20;   conn.close()

&#x20;   return {"rows": rows}



@app.route("/ping")

def ping():

&#x20;   host = request.args.get("host", "127.0.0.1")

&#x20;   result = run\_ping(host)

&#x20;   return result.stdout



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(debug=DEBUG)



