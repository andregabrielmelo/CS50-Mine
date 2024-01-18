SELECT title
FROM movies
JOIN stars ON movies.id = stars.movie_id
WHERE stars.person_id IN (
    SELECT id
    FROM people
    WHERE name in ('Bradley Cooper', 'Jennifer Lawrence')
)
GROUP BY title
HAVING COUNT(*) = 2
;
