-- https://www.hackerrank.com/contests/simply-sql/challenges/the-blunder
-- ms sql
select ceiling(avg(cast(salary as decimal) ) - avg(CAST(REPLACE(salary, 0, '') as decimal) )) from Employees