-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name as genre, count(sg.show_id) as number_of_shows FROM tv_genres g
INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;