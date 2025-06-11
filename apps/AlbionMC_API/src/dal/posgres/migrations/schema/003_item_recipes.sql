CREATE TABLE item_recipes (
    id SERIAL PRIMARY KEY,
    item_id INTEGER UNIQUE NOT NULL,
    silver_cost INTEGER NOT NULL,
    craft_time NUMERIC NOT NULL, 
    focus_cost NUMERIC NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL,
    data_source_id INTEGER NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (data_source_id) REFERENCES data_sources(id)
);

CREATE TABLE recipe_slots (
    recipe_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    item_count INTEGER NOT NULL,
    max_return INTEGER NOT NULL,
    PRIMARY KEY (recipe_id, item_id),
    FOREIGN KEY (recipe_id) REFERENCES item_recipes(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);