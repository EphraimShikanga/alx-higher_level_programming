-- displays max temp of each state
SELECT state,
    max(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

