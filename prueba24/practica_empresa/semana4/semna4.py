import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generamos datos aleatorios y los convertimos en un DataFrame
data = pd.DataFrame({'valores': np.random.randn(500)})

# Creamos el histograma
sns.histplot(data['valores'], bins=30, kde=True)

# Añadimos título y etiquetas
plt.title('Histograma con Seaborn')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostramos el gráfico
plt.show()
