import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Planilha_Excel_1 = "Planilha1e2.xlsx"
Planilha_Excel_2 = "Planilha3.xlsx"

df_dia_1 = pd.read_excel(
    Planilha_Excel_1, sheet_name='Dia 1')
df_dia_2 = pd.read_excel(
    Planilha_Excel_1, sheet_name='Dia 2')
df_dia_3 = pd.read_excel(
    Planilha_Excel_2, sheet_name='Dia 3')

df_todas_as_planilhas = pd.concat([df_dia_1, df_dia_2, df_dia_3])
df_todas_as_planilhas.to_excel('Todas_As_Planilhas.xlsx')

lucros_dos_vendededores = df_todas_as_planilhas.groupby(['Vendedor']).sum()

relatório = lucros_dos_vendededores.loc[:, "Unidades":"Preços"]

relatório.plot(kind='bar')

plt.show()
