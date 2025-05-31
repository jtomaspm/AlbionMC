CREATE TABLE data_sources (
    id SERIAL PRIMARY KEY,
    data_source_name VARCHAR(255) NOT NULL,
    trust_level SMALLINT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(60) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(60) NOT NULL
);
