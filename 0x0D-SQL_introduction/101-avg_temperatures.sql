-- displays avg temp by city ordered by temp
SELECT city,
    AVG(value) AS avg_temp
FROM temperatures
GROUP by CITY
ORDER BY avg_temp DESC;

