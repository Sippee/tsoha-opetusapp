from app import app
from flask import render_template, request, redirect
import users
import courses

@app.route("/")
def index():
    return render_template("index.html")   

@app.route("/addassignment", methods=["GET", "POST"])
def addassignment():
    users.require_role("opettaja")

    if request.method == "GET":
        return render_template("addassignment.html")

    if request.method == "POST":
        coursename = request.form["coursename"]
        name = request.form["name"]
        assignment = request.form["assignment"]
        answer = request.form["answer"]
        multichoice = request.form["multichoice"]
        option1 = request.form["option1"]
        option2 = request.form["option2"]
        option3 = request.form["option3"]
        try:
            courses.add_assignment(coursename, name, assignment,
                                    answer, multichoice,
                                    option1, option2, option3)
            return redirect("/courses")
        except:
            return redirect("/courses")

@app.route("/addmaterial", methods=["GET", "POST"])
def addmaterial():
    users.require_role("opettaja")

    if request.method == "GET":
        return render_template("addmaterial.html")

    if request.method == "POST":
        coursename = request.form["coursename"]
        materialname = request.form["materialname"]
        material = request.form["material"]
        try:
            courses.add_material(coursename, materialname, material)
            return redirect("/courses")
        except:
            return redirect("/courses")

@app.route("/changecourse", methods=["GET", "POST"])
def changecourse():
    users.require_role("opettaja")

    if request.method == "GET":
        return render_template("changecourse.html")

    if request.method == "POST":
        oldname = request.form["oldname"]
        newname = request.form["newname"]
        courses.change_course(oldname, newname)
        return redirect("/courses")

@app.route("/addcourse", methods=["GET", "POST"])
def addcourse():
    users.require_role("opettaja")

    if request.method == "GET":
        return render_template("addcourse.html")

    if request.method == "POST":
        name = request.form["name"]
        courses.add_course(name)
        return redirect("/courses")

@app.route("/removecourse", methods=["GET", "POST"])
def removecourse():
    users.require_role("opettaja")

    if request.method == "GET":
        return render_template("removecourse.html")

    if request.method == "POST":
        name = request.form["name"]
        courses.remove_course(name)
        return redirect("/courses")

@app.route("/answer", methods=["POST"])
def answer():
    if request.method == "POST":
        user_id = users.user_id()
        assignment_id = request.form["assignment_id"]
        correct_answer = request.form["answer"]
        courses.store_answer(user_id, assignment_id, correct_answer)
        return redirect("/assignment/"+assignment_id)

@app.route("/course/<int:course_id>")
def show_course(course_id):
    name = courses.get_coursename(course_id)
    materials = courses.get_materialsbycourse(course_id)
    assignments = courses.get_assignmentsbycourse(course_id)
    completed_assignments = courses.get_completed_assignments(users.user_id(), course_id)
    return render_template("course.html", course_id=course_id,
                           course_name=name,
                           material_list=materials,
                           assignment_list=assignments,
                           completed_list=completed_assignments)

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
                           assignment_answer=assignment[3],
                           assignment_multichoice=assignment[4],
                           assignment_option1=assignment[5],
                           assignment_option2=assignment[6],
                           assignment_option3=assignment[7])

@app.route("/join", methods=["POST"])
def joincourse():
    if request.method == "POST":
        user_id = users.user_id()
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