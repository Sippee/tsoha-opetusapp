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
        print(result,flush=True)
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
