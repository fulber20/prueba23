CREATE DATABASE tienda_comercio;

USE tienda_comercio;

CREATE TABLE historial_ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    producto VARCHAR(100),
    cantidad INT,
    precio_unitario DECIMAL(10, 2),
    total DECIMAL(10, 2)
);

INSERT INTO historial_ventas (fecha, producto, cantidad, precio_unitario, total) VALUES
('2024-01-01', 'Producto A', 5, 10.00, 50.00),
('2024-01-02', 'Producto B', 2, 15.00, 30.00),
('2024-01-03', 'Producto C', 10, 7.50, 75.00),
('2024-01-04', 'Producto A', 3, 10.00, 30.00),
('2024-01-05', 'Producto D', 1, 25.00, 25.00);
