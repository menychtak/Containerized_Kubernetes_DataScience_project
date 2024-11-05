CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL
);

INSERT INTO tasks (task) VALUES ('Task 1'), ('Task 2'), ('Task 3');