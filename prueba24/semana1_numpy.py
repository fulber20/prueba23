import numpy as np

# 1. Crear arrays NumPy
array1 = np.aray([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", array1)
print("Array 2:", array2)

# 2. Operaciones básicas
suma = array1 + array2
resta = array1 - array2
producto = array1 * array2
division = array2 / array1

print("\nSuma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)

# 3. Funciones matemáticas
# Calcular la media, desviación estándar y varianza
media = np.mean(array1)
desviacion_estandar = np.std(array1)
varianza = np.var(array1)

print("\nMedia de array1:", media)
print("Desviación estándar de array1:", desviacion_estandar)
print("Varianza de array1:", varianza)

# 4. Operaciones sobre arrays multidimensionales
# Crear un array 2D
array_2d = n.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nArray 2D:")
print(array_2d)

# Operaciones en arrays 2D
suma_filas = np.sum(array_2d, axis=1)  # Suma por filas
sma_columnas = np.sum(array_2d, axis=0)  # Suma por columnas

print("\nSuma por filas:", suma_filas)
print("Suma por columnas:", suma_columnas)

# Transponer el array 2D
array_2d_transpuesto = np.transpose(array_2d)
print("\nArray 2D transpuesto:")
print(array_2d_transpuesto)
