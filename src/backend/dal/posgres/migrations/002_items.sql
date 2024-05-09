CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    unique_name VARCHAR(60) DEFAULT '',
    english_name VARCHAR(60) DEFAULT '',
    tags VARCHAR(20)[] DEFAULT '{}'::VARCHAR[],
    tier TINYINT DEFAULT 0,
    enchant TINYINT DEFAULT 0,
    item_description VARCHAR(255) DEFAULT '',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(60) DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(60) DEFAULT '',
    data_source_id INTEGER NOT NULL,
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id)
);