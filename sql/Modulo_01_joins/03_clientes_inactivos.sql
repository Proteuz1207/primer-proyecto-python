SELECT
	clientes.nombre_cliente,
	ordenes.id_orden
from clientes
LEFT JOIN ordenes
on clientes.id_cliente = ordenes.id_cliente
where ordenes.id_cliente is NULL;