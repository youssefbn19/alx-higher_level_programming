-- List all genres not linked to the show Dexter.
SELECT name FROM tv_genres
WHERE id NOT IN (
SELECT sg.genre_id FROM tv_show_genres sg
JOIN tv_shows s
ON s.id = sg.show_id
WHERE s.title = "Dexter")
ORDER BY name;
