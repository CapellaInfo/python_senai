import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('PythonClass8/filmes.xlsx')


# plt.scatter(df['Nome'], df['Avaliacao'], color='green', alpha=0.5)  # Plotar gráfico de dispersão
# plt.xticks(rotation=45)
# plt.show()

# sns.violinplot(x = 'Ano', y = 'Avaliacao', data=df)
# plt.show()

# sns.boxplot(x = 'Ano', y = 'Avaliacao', data=df)
# plt.show()

# sns.barplot(x = 'Avaliacao', y = 'Nome', data=df)
# plt.show()

grouped = df.groupby('Ano').size().reset_index(name='Count')

labels = grouped['Ano']
sizes = grouped['Count']
colors = sns.color_palette('pastel')[0:len(labels)]

plt.pie(sizes, labels=labels, colors=colors, autopct='%.0f%%')
plt.axis('equal')
plt.show()

