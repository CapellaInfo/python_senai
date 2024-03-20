import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('PythonClass8/filmes.xlsx')


plt.scatter(df['Nome'], df['Avaliacao'], color='green', alpha=0.5)  # Plotar gráfico de dispersão
plt.xticks(rotation=45)
plt.show()

sns.violinplot(x = 'Ano', y = 'Avaliacao', data=df)
plt.show()

sns.boxplot(x = 'Ano', y = 'Avaliacao', data=df)
plt.show()



