# Write your MySQL query statement below

#SELECT MIN(salary) AS SecondHighestSalary FROM (SELECT * FROM Employee ORDER BY salary DESC LIMIT 2) AS tmp


SELECT COALESCE( (SELECT DISTINCT salary as SecondHighestSalary FROM Employee 
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary