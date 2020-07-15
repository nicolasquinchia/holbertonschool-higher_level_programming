-- List all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_genres.name
FROM tv_genres
    WHERE name not in (
    SELECT tv_genres.name
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_shows.title = "Dexter")
    ORDER BY tv_genres.name ASC;
