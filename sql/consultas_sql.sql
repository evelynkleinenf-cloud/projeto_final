-- ============================================
-- QUERY 1
-- Funcionários, cargos e departamentos
-- ============================================

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    e.salary,
    j.job_title,
    d.department_name
FROM hr.employees e
LEFT JOIN hr.jobs j
    ON e.job_id = j.job_id
LEFT JOIN hr.departments d
    ON e.department_id = d.department_id
WHERE e.salary IS NOT NULL
ORDER BY e.salary DESC;
-- ============================================
-- QUERY 2
-- Funcionários, departamentos e localização
-- ============================================

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    c.country_name,
    r.region_name
FROM hr.employees e
LEFT JOIN hr.departments d
    ON e.department_id = d.department_id
LEFT JOIN hr.locations l
    ON d.location_id = l.location_id
LEFT JOIN hr.countries c
    ON l.country_id = c.country_id
LEFT JOIN hr.regions r
    ON c.region_id = r.region_id
WHERE d.department_name IS NOT NULL
ORDER BY r.region_name, c.country_name, l.city;