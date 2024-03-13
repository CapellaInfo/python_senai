import pandas as pd

igm_df = pd.read_csv("PythonClass7/APlicacaoMunicipios/igm_modificado.csv")

print(igm_df.head())
print(igm_df.shape)
print(igm_df.info())
print(igm_df.tail())
print(igm_df.sample(5))
print(igm_df.sample(5).T)
print(igm_df[0:5].T)
print(igm_df[-5:].T)
print(igm_df[20:30])
print(igm_df['porte'])
print(igm_df['porte'].value_counts())
ind_des = igm_df['indice_governanca']
ind_des.count()
ind_des.size
ind_des.isnull()
ind_des.isnull().sum()
ind_des.dropna()
ind_des.isnull().sum()
ind_des.dropna(inplace=True)
ind_des.isnull().sum()
ind_des.min()
ind_des.max()
ind_des.mean()
ind_des.std()
ind_des.describe()
igm_df.describe()
print(igm_df[igm_df['regiao']=='NORDESTE'])


limeira = igm_df[igm_df['municipio']=='LIMEIRA']
print(limeira.T)