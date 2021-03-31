-- Insights from Data with BigQuery: Challenge Lab

-- 1
SELECT
  sum(cumulative_confirmed) AS total_cases_worldwide 
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date = '2020-04-15'

-- 2
WITH deaths_by_state AS (
  SELECT
    subregion1_code AS state,
    SUM(cumulative_deceased) AS death_count
  FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE date = '2020-04-10' 
    AND country_name = 'United States of America'
    AND subregion1_code IS NOT NULL
  GROUP BY subregion1_code
)
SELECT
  COUNT(death_count) AS count_of_states
FROM deaths_by_state 
WHERE
  death_count > 100
;

-- 3
SELECT
  subregion1_name AS state,
  SUM(cumulative_confirmed) AS total_confirmed_cases
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date = '2020-04-10'
  AND country_name = 'United States of America'
  AND subregion1_code IS NOT NULL
GROUP BY subregion1_name
HAVING total_confirmed_cases > 1000
ORDER BY total_confirmed_cases DESC
;

-- 4. 아래가 맞는 것 같은데...
SELECT
  SUM(cumulative_confirmed) AS total_confirmed_cases,
  SUM(cumulative_deceased) AS total_deaths,
  SUM(cumulative_deceased) / SUM(cumulative_confirmed) * 100 AS case_fatality_ratio
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date BETWEEN "2020-04-01" AND "2020-04-30"
  AND country_name = "Italy"
;

SELECT
  SUM(new_confirmed) AS total_confirmed_cases,
  SUM(new_deceased) AS total_deaths,
  SUM(new_deceased) / SUM(new_confirmed) * 100 AS case_fatality_ratio
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date BETWEEN "2020-04-01" AND "2020-04-30"
  AND country_name = "Italy"
;

-- 5. 어 이게 왜 되는거지?
SELECT
  date
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_name = "Italy"
  AND cumulative_deceased > 10000
ORDER BY date
LIMIT 1
;


-- 6
WITH india_cases_by_date AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="India"
    AND date between '2020-02-21' and '2020-03-15'
  GROUP BY date
  ORDER BY date ASC
), india_previous_day_comparison AS (
  SELECT
    date,
    cases,
    LAG(cases) OVER(ORDER BY date) AS previous_day,
    cases - LAG(cases) OVER(ORDER BY date) AS net_new_cases
  FROM india_cases_by_date
)
SELECT
  COUNT(date) AS zero_increase_days
FROM india_previous_day_comparison
WHERE net_new_cases = 0;

-- 7
WITH us_cases_by_date AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="United States of America"
    AND date between '2020-03-22' and '2020-04-20'
  GROUP BY date
  ORDER BY date ASC
), us_previous_day_comparison AS (
  SELECT
    date AS Date,
    cases AS Confirmed_Cases_On_Day,
    LAG(cases) OVER(ORDER BY date) AS Confirmed_Cases_Previous_Day,
    (cases / LAG(cases) OVER(ORDER BY date) - 1) * 100 AS Percentage_Increase_In_Cases
  FROM us_cases_by_date
)
SELECT
  *
FROM us_previous_day_comparison
WHERE Percentage_Increase_In_Cases > 10
;

-- 8
SELECT
  country_name AS country,
  SUM(cumulative_recovered) AS recovered_cases,
  SUM(cumulative_confirmed) AS confirmed_cases,
  SUM(cumulative_recovered) / SUM(cumulative_confirmed) * 100 AS recovery_rate
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE date = '2020-05-10'
GROUP BY country_name
HAVING confirmed_cases > 50000
ORDER BY recovery_rate DESC
LIMIT 10
;

-- 9
WITH france_cases AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS total_cases
  FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name = "France"
    AND date IN ('2020-01-24', '2020-05-10')
  GROUP BY date
  ORDER BY date
), summary as (
  SELECT
    total_cases AS first_day_cases,
    LEAD(total_cases) OVER(ORDER BY date) AS last_day_cases,
    DATE_DIFF(LEAD(date) OVER(ORDER BY date), date, day) AS days_diff
  FROM
    france_cases
  LIMIT 1
)
SELECT 
  first_day_cases,
  last_day_cases,
  days_diff,
  POWER(last_day_cases / first_day_cases, 1 / days_diff) - 1 AS cdgr
FROM summary
