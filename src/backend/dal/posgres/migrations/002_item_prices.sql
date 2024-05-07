CREATE TABLE item_prices (
    item_id INTEGER NOT NULL,
    price INTEGER NOT NULL,
    city VARCHAR(100) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    PRIMARY KEY (item_id, created_at),
    FOREIGN KEY (item_id) REFERENCES items(id)
);