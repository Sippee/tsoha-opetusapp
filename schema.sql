CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT,
    role TEXT
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE participants (
    user_id INTEGER REFERENCES users,
    course_id INTEGER REFERENCES courses
);