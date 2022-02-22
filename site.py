from flask import Flask, request, render_template, redirect
import datetime

import api

app = Flask("app")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/homework/new", methods=["GET", "POST"])
def new():
    if request.method.upper() == "GET":
        return render_template("new.html")
    elif request.method.upper() == "POST":
        if None in [request.form.get("subject"),request.form.get("todo"),request.form.get("enddate")]:
            return redirect("/new")
        api.write_homeworks(request.form["subject"], request.form["todo"], request.form["enddate"].split("-"))
        return redirect("/homework")

@app.route("/homework")
def homework():
    return render_template("homework.html")

@app.route("/homework/work")
def work():
    return api.getwork()
        
@app.route("/subjects")
def subjects():
    return ",".join(["Biologie", "Deutsch", "Englisch", "Geography", "History", "Kunst", "Latein", "Mathe", "Philosophie", "Physik"])
    
@app.route("/homework/done_change", methods=["POST"])
def done_change():
    d = request.data.decode().split(",")
    return str(api.setdone(d[0], d[1]=="true"))
    
app.run("127.0.0.1", 5000)
