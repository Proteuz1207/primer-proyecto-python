-- ====================================================================
-- MODULE 02: DATABASE DESIGN & ARCHITECTURE (DDL)
-- LAB 01: CREATING MASTER TABLES AND CONSTRAINTS
-- ====================================================================

-- 1. CONFIGURACIÓN DEL ENTORNO (Siempre arriba)
PRAGMA foreign_keys = ON;

-- Limpieza preventiva para permitir la re-ejecución del script
DROP TABLE IF EXISTS colaboradores;
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS departamentos;

-- ====================================================================
-- 2. DEFINICIÓN DE ESTRUCTURAS (DDL)
-- ====================================================================

-- Tabla Maestra Independiente A (Laboratorio de restricciones básicas)
CREATE TABLE empleados (
    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL CHECK(salario > 0),
    fecha_ingreso TEXT DEFAULT CURRENT_DATE
);

-- Tabla Maestra Independiente B
CREATE TABLE departamentos (
    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_depto TEXT NOT NULL UNIQUE
);

-- Tabla Dependiente (Relación Entidad-Relación)
CREATE TABLE colaboradores (
    id_colaborador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    id_departamento INTEGER,
    -- Configuración del candado de integridad referencial
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
    ON DELETE RESTRICT
);

-- ====================================================================
-- 3. INSERCIÓN DE DATOS DE CONTROL
-- ====================================================================

INSERT INTO departamentos (nombre_depto) VALUES ('Tecnología'); 

INSERT INTO colaboradores (nombre, id_departamento) VALUES ('Gabriel Martinez', 1);

-- ====================================================================
-- 4. REGISTRO DE AUDITORÍA (PRUEBAS DE LABORATORIO)
-- ====================================================================

-- NOTA DE INGENIERÍA: El siguiente comando está comentado porque el diseño 
-- de la base de datos bloquea el borrado con un "FOREIGN KEY constraint failed".
-- Para probar el candado, descomenta la línea e intenta ejecutarla:

-- DELETE FROM departamentos WHERE id_departamento = 1;