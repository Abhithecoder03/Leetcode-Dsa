SELECT id
FROM (
    SELECT id, recordDate, temperature,
           LAG(temperature) OVER (ORDER BY recordDate) AS previous_temperature,
           LAG(recordDate) OVER (ORDER BY recordDate) AS previous_date
    FROM Weather
) subquery
WHERE temperature > previous_temperature AND DATEDIFF(recordDate,previous_date)=1;