import numpy as np

array1d = np.array([1, 2, 3, 4, 5])
print("Array 1D:")
print(array1d)

# Crear un array de 2D
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray 2D:")
print(array2d)

# Operaciones matemáticas
suma = array1d + 10
print("\nArray 1D después de sumar 10:")
print(suma)

producto = array2d * 2
print("\nArray 2D después de multiplicar por 2:")
print(producto)

# Estadísticas básicas
media = np.mean(array2d)
print("\nMedia de los elementos del array 2D:")
print(media)

# Transponer un array 2D
transpuesto = np.transpose(array2d)
print("\nArray 2D transpuesto:")
print(transpuesto)

# Crear un array con valores aleatorios
aleatorios = np.random.random((3, 3))
print("\nArray 3x3 con valores aleatorios:")
print(aleatorios)

# Operaciones de álgebra lineal
matriz = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])
producto_matriz_vector = np.dot(matriz, vector)
print("\nProducto de la matriz con el vector:")
print(producto_matriz_vector)
