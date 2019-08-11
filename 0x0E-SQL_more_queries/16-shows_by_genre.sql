-- list all shows that a linked by genre to another
-- if they have same genre
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv genres ON tve_show_genres.genre.id - tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
