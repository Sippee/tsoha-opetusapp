from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
    sql = "SELECT id, name, password, role FROM users WHERE name=:name"
    result = db.session.execute(text(sql), {"name":name})
    user = result.fetchone()

    if not user:
        return False
    if not check_password_hash(user[2], password):
        return False

    session["user_id"] = user[0]
    session["user_name"] = user[1]
    session["user_role"] = user[3]

    return True

def register(name, password, role):
    hashed_password = generate_password_hash(password)

    try:
        sql = """INSERT INTO users (name, password, role)
                 VALUES (:name, :password, :role)"""
        db.session.execute(text(sql), {"name":name, "password":hashed_password, "role":role})
        db.session.commit()
    except:
        return False

    return login(name, password)

def logout():
    session.clear()