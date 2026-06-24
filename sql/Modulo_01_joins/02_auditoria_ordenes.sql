-- ====================================================================
-- MODULE 01: RELATIONAL MECHANICS & COMPLEX UNIFICATIONS
-- AUDIT: IDENTIFYING ORPHANED ORDERS IN THE SYSTEM
-- ====================================================================

SELECT  
    ordenes.id_orden,
    ordenes.producto, 
    ordenes.monto,
    clientes.nombre_cliente
FROM ordenes
LEFT JOIN clientes
    ON ordenes.id_cliente = clientes.id_cliente
WHERE clientes.id_cliente IS NULL;