from openpyxl import Workbook
wb = Workbook()

planilha = wb.worksheets[0]

planilha['A1'] = "Dia"
planilha['B1'] = "Vendedor"
planilha['C1'] = "Produto"
planilha['D1'] = "Unidades"
planilha['E1'] = "Preços"

planilha.title = 'Dia 3'

wb.save("C:/Users/55859/Documents/Projetos/Projetos_Python/Planilha3.xlsx")
