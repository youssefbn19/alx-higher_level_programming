-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name as genre, count(*) as number_of_shows FROM tv_show_genres sg
INNER JOIN tv_genres g
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
