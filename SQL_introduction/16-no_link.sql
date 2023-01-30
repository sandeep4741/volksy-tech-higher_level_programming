-- list the all data
SELECT score, name FROM second_table
WHERE name IS NOT NULL
order by score DESC;
