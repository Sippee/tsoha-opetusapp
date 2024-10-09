from db import db
from sqlalchemy.sql import text

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
    WHERE a.id=:assignment_id"""
    result = db.session.execute(text(sql1),{"assignment_id":assignment_id}).fetchone()
    if result[0]==correct_answer:
        sql2 = """INSERT INTO answers (user_id, assignment_id, answer) 
        VALUES (:user_id, :assignment_id, :answer)"""
        db.session.execute(text(sql2),{"user_id":user_id, "assignment_id":assignment_id, "answer":correct_answer})
        db.session.commit()
        return True

    return False