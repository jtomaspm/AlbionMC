CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    tags VARCHAR(255)[] DEFAULT '{}'::VARCHAR[],
    tier INTEGER,
    enchant INTEGER,
    item_description VARCHAR(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL
);