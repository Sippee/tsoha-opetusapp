from db import db
from sqlalchemy.sql import text

def add_material(course_name, name, material):
    sql = """INSERT INTO materials (course_id, name, material)
    VALUES ((SELECT id FROM courses WHERE name=:course_name), :name, :material)"""
    db.session.execute(text(sql),{"course_name":course_name, "name":name, "material":material})
    db.session.commit()

def change_course(oldname, newname):
    sql1 = """SELECT id, name FROM courses WHERE name=:name"""
    result = db.session.execute(text(sql1),{"name":oldname}).fetchone()
    if result and result[1]==oldname:
        sql2 = """UPDATE courses SET name=:name WHERE id=:id"""
        db.session.execute(text(sql2),{"name":newname, "id":result[0]})
        db.session.commit()
        return True

    return False

def add_course(name):
    sql1 = """SELECT name FROM courses WHERE name=:name"""
    result = db.session.execute(text(sql1),{"name":name}).fetchone()
    if result==None or result[0]!=name:
        sql2 = """INSERT INTO courses (name) 
        VALUES (:name)"""
        db.session.execute(text(sql2),{"name":name})
        db.session.commit()
        return True

    return False

def remove_course(name):
    sql1 = """SELECT name FROM courses WHERE name=:name"""
    result = db.session.execute(text(sql1),{"name":name}).fetchone()

    if result and result[0]==name:
        sql2 = """DELETE FROM courses WHERE name=:name"""
        db.session.execute(text(sql2),{"name":name})
        db.session.commit()
        return True

    return False

def get_courses():
    sql = """SELECT id, name FROM courses"""
    return db.session.execute(text(sql)).fetchall()

def join_course(user_id, course_id):
    sql1 = """SELECT user_id, course_id FROM participants
    WHERE user_id=:user_id and course_id=:course_id"""
    result = db.session.execute(text(sql1),{"user_id":user_id, "course_id":course_id}).fetchone()
    if result==None or result[0]!=int(user_id) and result[1]!=int(course_id):
        sql2 = """INSERT INTO participants (user_id, course_id) 
        VALUES (:user_id, :course_id)"""
        db.session.execute(text(sql2),{"user_id":user_id, "course_id":course_id})
        db.session.commit()
        return True

    return False

def get_coursename(course_id):
    sql = """SELECT name FROM courses c WHERE c.id=:course_id"""
    result = db.session.execute(text(sql),{"course_id":course_id}).fetchone()
    return result

def get_materialsbycourse(course_id):
    sql = """SELECT id, name FROM materials m WHERE m.course_id=:course_id"""
    result = db.session.execute(text(sql),{"course_id":course_id}).fetchall()
    return result

def get_assignmentsbycourse(course_id):
    sql = """SELECT id, name FROM assignments a WHERE a.course_id=:course_id"""
    result = db.session.execute(text(sql),{"course_id":course_id}).fetchall()
    return result

def get_material(material_id):
    sql = """SELECT course_id, name, material FROM materials m WHERE m.id=:material_id"""
    result = db.session.execute(text(sql),{"material_id":material_id}).fetchone()
    return result

def get_assignment(assignment_id):
    sql = """SELECT course_id, name, assignment, answer FROM assignments a WHERE a.id=:assignment_id"""
    result = db.session.execute(text(sql),{"assignment_id":assignment_id}).fetchone()
    return result

def store_answer(user_id, assignment_id, correct_answer):
    sql1 = """SELECT answer FROM assignments a
    WHERE id=:assignment_id"""
    result = db.session.execute(text(sql1),{"assignment_id":assignment_id}).fetchone()

    sql2 = """SELECT user_id, assignment_id FROM answers
    WHERE user_id=:user_id and assignment_id=:assignment_id"""
    result2 = db.session.execute(text(sql2),{"user_id":user_id,"assignment_id":assignment_id}).fetchone()

    if result2==None or result2[0]!=int(user_id) and result2[1]!=int(assignment_id):
        if result[0]==correct_answer:
            sql3 = """INSERT INTO answers (user_id, assignment_id, answer) 
            VALUES (:user_id, :assignment_id, :answer)"""
            db.session.execute(text(sql3),{"user_id":user_id, "assignment_id":assignment_id, "answer":correct_answer})
            db.session.commit()
            return True

    return False

def get_completed_assignments(user_id, course_id):
    sql1 = """SELECT a.id, a.name FROM assignments a, answers b
    WHERE a.id=b.assignment_id and a.answer=b.answer and
    a.course_id=:course_id and b.user_id=:user_id"""
    result = db.session.execute(text(sql1),{"course_id":course_id,"user_id":user_id}).fetchall()
    return result