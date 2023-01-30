-- count
SELECT score, COUNT(score) AS number FROM second_table
group by score,
order by score desc;
