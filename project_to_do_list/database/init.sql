CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL UNIQUE,  -- Ensure each task description is unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Automatically set the creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Automatically set the update timestamp
    completed BOOLEAN DEFAULT FALSE  -- Track task completion status
);

-- Insert sample tasks with current timestamps
INSERT INTO tasks (task) 
VALUES 
    ('Create containers'), 
    ('Use Kubernetes'), 
    ('Complete docker project');
