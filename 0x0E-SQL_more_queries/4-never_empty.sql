-- Creates the table id_not_null on current MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256));