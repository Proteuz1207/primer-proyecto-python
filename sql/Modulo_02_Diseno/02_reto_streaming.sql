-- ====================================================================
-- MODULE 02: DATABASE DESIGN & ARCHITECTURE (DDL)
-- RETO DE CIERRE: STREAMING PLATFORM DATABASE DESIGN
-- ====================================================================

-- 1. CONFIGURACIÓN DEL ENTORNO
PRAGMA foreign_keys = ON;

-- Limpieza preventiva (Primero la tabla hija, luego la madre)
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS planes;

-- ====================================================================
-- 2. DEFINICIÓN DE ESTRUCTURAS (DDL)
-- ====================================================================

CREATE TABLE planes (
    id_plan INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_plan TEXT NOT NULL UNIQUE,
    precio_mensual REAL CHECK (precio_mensual > 0)    
);

CREATE TABLE usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    id_plan INTEGER,
    FOREIGN KEY (id_plan) REFERENCES planes (id_plan)
    ON DELETE RESTRICT
);

-- ====================================================================
-- 3. INSERCIÓN DE DATOS DE CONTROL (DML)
-- ====================================================================

INSERT INTO planes (nombre_plan, precio_mensual)
VALUES ("Premium", 10.99);

INSERT INTO usuarios (nombre_usuario, id_plan, correo)
VALUES ("Gabriel Martinez", 1, "proteuz1207@gmail.com");

-- ====================================================================
-- 4. PRUEBAS DE ESTRÉS (RESTRICCIONES)
-- ====================================================================

-- PRUEBA 1: Bloqueada por violación de Llave Foránea (Plan inexistente)
-- INSERT INTO usuarios (nombre_usuario, id_plan, correo) VALUES ("Intruso", 999, "intruso@mail.com");

-- PRUEBA 2: Bloqueada por ON DELETE RESTRICT (Plan con usuarios activos)
-- DELETE FROM planes WHERE id_plan = 1;