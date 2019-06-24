import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MICRODADOS_ENEM_2018.csv', sep=';', encoding='latin-1')

sns.set(style="whitegrid")
ax = sns.countplot(x="SG_UF_RESIDENCIA", hue='TP_SEXO', data=df)

plt.show()
