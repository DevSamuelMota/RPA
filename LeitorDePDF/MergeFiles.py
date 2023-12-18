import PyPDF2
import re

# Abrindo arquivos modo binário e leitura
arquivo_1 = open(
    "C:/Users/55859/Documents/Projetos/Projetos_Python/LeitorDePDF/Acessibilidade.pdf", 'rb')
arquivo_2 = open(
    "C:/Users/55859/Documents/Projetos/Projetos_Python/LeitorDePDF/Planilha3.pdf", 'rb')
# Lendo os dados do binario em PDF
dados_do_arq1 = PyPDF2.PdfReader(arquivo_1)
dados_do_arq2 = PyPDF2.PdfReader(arquivo_2)

# Declarando um objeto do tipo Merge
merge = PyPDF2.PdfMerger()

# Aplicando append nos meus merge dos meus dados de pdf
merge.append = (dados_do_arq1)
merge.append = (dados_do_arq2)
# Escrevendo um novo Arquivo Pdf
merge.write(
    'C:/Users/55859/Documents/Projetos/Projetos_Python/LeitorDePDF/ArquivoMerge.pdf')
