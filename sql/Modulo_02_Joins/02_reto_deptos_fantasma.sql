-- Módulo 2: Relaciones y Uniones Complejas
-- Ejercicio: Identificar departamentos sin empleados asignados (Auditoría de registros huérfanos)

SELECT 
    departamentos.id_departamento,
    departamentos.nombre_depto,
    empleados.nombre_empleado
FROM departamentos
LEFT JOIN empleados 
    ON departamentos.id_departamento = empleados.id_departamento
WHERE empleados.nombre_empleado IS NULL;