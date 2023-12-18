import PyPDF2
import re
# Abrindo arquivo em modo de leitura e retornando o binário
pdf_file = open(
    "C:/Users/55859/Documents/Projetos/Projetos_Python/LeitorDePDF/Acessibilidade.pdf", "rb")

# Pegamos os dados do binário e armazenamos na variável pdf_file e atribuímos os dados de leitura
dados_do_pdf = PyPDF2.PdfReader(pdf_file)

numero_de_paginas = len(dados_do_pdf.pages)

print(f"O PDF possui {numero_de_paginas} páginas")

# Obtendo a primeira página (índice 0)
pagina_1 = dados_do_pdf.pages[0]

# Pegando o texto extraído da página 1
texto_da_pagina1 = pagina_1.extract_text()

print(texto_da_pagina1)
texto_da_pagina1 = re.sub("\n", '', texto_da_pagina1)
pdf_file.close()  # Certifique-se de fechar o arquivo após o uso
