-- Creates the table id_not_null on current MySQL server.
CREATE TABLE IF NOT EXISTS force_name(
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256));