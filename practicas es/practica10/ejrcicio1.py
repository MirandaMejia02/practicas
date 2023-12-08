import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    'puntaje_exam1': [85, 90, 78, 92, 88],
    'puntaje_exam2': [70, 85, 92, 76, 80]
}

# Crea un DataFrame con los datos
df = pd.DataFrame(data)

# Crea el gráfico de áreas para la relación entre puntajes
plt.fill_between(df['puntaje_exam1'], df['puntaje_exam2'], alpha=0.5)
plt.xlabel('Puntaje del Examen 1')
plt.ylabel('Puntaje del Examen 2')
plt.title('Relación entre Puntajes de dos Exámenes')

# Muestra el gráfico
plt.show()