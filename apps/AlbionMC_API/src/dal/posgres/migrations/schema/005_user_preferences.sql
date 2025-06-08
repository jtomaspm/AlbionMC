CREATE TABLE user_preferences (
    user_id INTEGER NOT NULL,
    theme VARCHAR(20) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(60) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(60) NOT NULL,
    PRIMARY KEY (user_id)
);