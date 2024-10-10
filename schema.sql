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

CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    name TEXT UNIQUE,
    material TEXT
);

CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    name TEXT UNIQUE,
    assignment TEXT,
    answer TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    assignment_id INTEGER REFERENCES assignments,
    answer TEXT
);