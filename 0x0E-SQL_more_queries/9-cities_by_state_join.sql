-- Lists all cities contained in current database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id

SELECT id, name FROM cities JOIN name FROM states
ORDER BY cities.id ASC;
