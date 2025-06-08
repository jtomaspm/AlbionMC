CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    unique_name VARCHAR(255) UNIQUE NOT NULL DEFAULT '',
    english_name VARCHAR(255) DEFAULT '',
    tags VARCHAR(20)[] DEFAULT '{}'::VARCHAR[],
    tier SMALLINT DEFAULT 0,
    enchant SMALLINT DEFAULT 0,
    item_description VARCHAR(255) DEFAULT '',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(60) DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(60) DEFAULT '',
    data_source_id INTEGER NOT NULL,
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id)
);