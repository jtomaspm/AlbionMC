CREATE TABLE crafting_slots (
    craft_id INTEGER NOT NULL,
    destination_item_id INTEGER NOT NULL,
    source_item_id INTEGER NOT NULL,
    source_item_quantity INTEGER NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    data_source_id INTEGER NOT NULL,
    PRIMARY KEY (craft_id, destination_item_id, source_item_id),
    FOREIGN KEY (destination_item_id) REFERENCES items(id),
    FOREIGN KEY (source_item_id) REFERENCES items(id),
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id)
);