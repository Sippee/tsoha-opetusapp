from app import app
from flask import render_template, request, redirect
import users
import courses

@app.route("/")
def index():
    return render_template("index.html")   

@app.route("/answer", methods=["POST"])
def answer():
    if request.method == "POST":
        user_id = request.form["user_id"]
        assignment_id = request.form["assignment_id"]
        correct_answer = request.form["answer"]
        try:
            courses.store_answer(user_id, assignment_id, correct_answer)
            return redirect("/assignment/"+assignment_id)
        except:
            return redirect("/assignment/"+assignment_id)

@app.route("/course/<int:course_id>")
def show_course(course_id):
    name = courses.get_coursename(course_id)
    materials = courses.get_materialsbycourse(course_id)
    assignments = courses.get_assignmentsbycourse(course_id)
    return render_template("course.html", course_id=course_id,
                           course_name=name,
                           material_list=materials,
                           assignment_list=assignments)

@app.route("/material/<int:material_id>")
def show_material(material_id):
    material = courses.get_material(material_id)
    return render_template("material.html", material_id=material_id,
                           course_id=material[0],
                           material_name=material[1],
                           material_text=material[2])

@app.route("/assignment/<int:assignment_id>")
def show_assignment(assignment_id):
    assignment = courses.get_assignment(assignment_id)
    return render_template("assignment.html", assignment_id=assignment_id, 
                           course_id=assignment[0],
                           assignment_name=assignment[1],
                           assignment_text=assignment[2],
                           assignment_answer=assignment[3])

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