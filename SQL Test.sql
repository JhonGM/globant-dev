-- Primer punto

SELECT job,
       department,
       [1] AS Q1,
       [2] AS Q2,
       [3] AS Q3,
       [4] AS Q4
from
(
    SELECT j.job,
           d.department,
           h.name,
           DATEPART(qq, CAST(h.datetime AS datetime)) AS datetime_format
    FROM [dbo].[hired_employees] h
        INNER JOIN jobs j
            ON h.job_id = j.id
        INNER JOIN departments d
            ON d.id = h.department_id
    WHERE DATEPART(YYYY, CAST(h.datetime AS datetime)) <= '2021'
) t
PIVOT
(
    COUNT(name)
    FOR datetime_format IN ([1], [2], [3], [4])
) AS PivotTable
ORDER BY 2,
         1


-- Segundo Punto
WITH departments_employees (id, department, hired)
AS (SELECT d.id,
           d.department,
           COUNT(h.name) AS hired
    FROM [dbo].[hired_employees] h
        INNER JOIN departments d
            ON d.id = h.department_id
    WHERE DATEPART(YYYY, CAST(h.datetime AS datetime)) <= '2021'
    GROUP BY d.id,
             d.department
   )
SELECT *
FROM departments_employees
WHERE hired >
(
    SELECT AVG(hired) FROM departments_employees
)