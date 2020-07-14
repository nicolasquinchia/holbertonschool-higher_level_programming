-- lists some records of the table second_table of the database, no Null names, desc order
SELECT score, name,
    FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
