# Importar las librerías necesarias
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Cargar y preparar el conjunto de datos
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0

# Crear el modelo
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Convertir las imágenes 2D en 1D
    Dense(128, activation='relu'),  # Capa densa con 128 neuronas y función de activación ReLU
    Dense(10, activation='softmax') # Capa de salida con 10 neuronas para clasificar 10 dígitos
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'\nPrecisión en el conjunto de pruebas: {test_acc}')