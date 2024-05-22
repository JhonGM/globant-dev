-- Primer Punto

SELECT 
    job,
    department,
    SUM(CASE WHEN quarter = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN quarter = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN quarter = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN quarter = 4 THEN 1 ELSE 0 END) AS Q4
FROM (
    SELECT 
        j.job,
        d.department,
        h.name,
        QUARTER(h.datetime) AS quarter
    FROM hired_employees h
    INNER JOIN jobs j ON h.job_id = j.id
    INNER JOIN departments d ON d.id = h.department_id
    WHERE YEAR(h.datetime) <= 2021
) AS t
GROUP BY job, department
ORDER BY department, job;

-- Segundo Punto

SELECT *
FROM (
    SELECT d.id,
           d.department,
           COUNT(h.name) AS hired
    FROM hired_employees h
    INNER JOIN departments d ON d.id = h.department_id
    WHERE YEAR(h.datetime) <= 2021
    GROUP BY d.id, d.department
) AS departments_employees
WHERE hired > (
    SELECT AVG(hired)
    FROM (
        SELECT d.id,
               d.department,
               COUNT(h.name) AS hired
        FROM hired_employees h
        INNER JOIN departments d ON d.id = h.department_id
        WHERE YEAR(h.datetime) <= 2021
        GROUP BY d.id, d.department
    ) AS subquery
);
