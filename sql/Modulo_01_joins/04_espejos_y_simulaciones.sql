SELECT
	clientes.nombre_cliente,
	ordenes.id_orden,ordenes.producto
from ordenes
LEFT JOIN  clientes
on clientes.id_cliente = ordenes.id_cliente

UNION 

SELECT
	clientes.nombre_cliente,
	ordenes.id_orden,ordenes.producto
from clientes
LEFT JOIN ordenes 
on clientes.id_cliente = ordenes.id_cliente
