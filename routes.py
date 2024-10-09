from app import app
from flask import render_template, request, redirect
import users
import courses

@app.route("/")
def index():
    return render_template("index.html")   

@app.route("/course/<int:course_id>")
def show_course(course_id):
    name = courses.get_coursename(course_id)
    return render_template("course.html", course_name=name)

@app.route("/join", methods=["POST"])
def joincourse():
    if request.method == "POST":
        user_id = request.form["user_id"]
        course_id = request.form["course_id"]
        try:
            courses.join_course(user_id, course_id)
            return redirect("/course/"+course_id)
        except:
            return redirect("/course/"+course_id)

@app.route("/courses")
def course():
    listofcourses = courses.get_courses()
    return render_template("/courses.html", list=listofcourses)

@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("login.html", message="Väärä tunnus tai salasana")
        return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        if not users.register(username, password, role):
            return render_template("register.html", message="Rekisteröinti ei onnistunut")

        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")