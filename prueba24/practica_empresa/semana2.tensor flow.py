import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection 
import train_test_split
from sklearn.naive_bayes
import MultinomialNB
from sklearn.metrics 
import accuracy_score, classification_report
import nltk
from nltk.corpus 
import stopwords
import re

# Descargamos el conjunto de stopwords
nltk.download('stopwords')

# Datos de ejemplo (reseñas y sus etiquetas)
data = {
    'review': [
        'Me encanta este teléfono, es excelente.',
        'El producto es horrible, no lo recomiendo.',
        'El teléfono es bueno pero podría mejorar.',
        'Muy satisfecho con la compra, excelente calidad.',
        'No me gustó, la batería dura muy poco.',
        'Es un buen teléfono a un precio razonable.',
        'Servicio al cliente fue terrible, pero el producto es bueno.',
        'Definitivamente no vale la pena, es muy malo.'
    ],
    'sentiment': [
        'positivo', 'negativo', 'neutral', 'positivo', 'negativo', 'positivo', 'neutral', 'negativo'
    ]
}

# Convertimos el diccionario a un DataFrame
df = pd.DataFrame(data)

# Preprocesamiento de texto
def preprocess_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar caracteres no alfabéticos
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Eliminar palabras de stopwords
    stop_words = set(stopwords.words('spanish'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Aplicar el preprocesamiento a las reseñas
df['review'] = df['review'].apply(preprocess_text)

# Vectorización del texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['positivo', 'negativo', 'neutral'])

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)

# Ejemplo de predicción
example_review = 'El teléfono es increíble y funciona muy bien'
example_review_preprocessed = preprocess_text(example_review)
example_vector = vectorizer.transform([example_review_preprocessed])
prediction = model.predict(example_vector)

print(f'La reseña "{example_review}" fue clasificada como: {prediction[0]}')
