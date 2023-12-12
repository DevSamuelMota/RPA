import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'}

page = requests.get("https://www.google.com/search?q=dolar&sca_esv=588364199&sxsrf=AM9HkKkgGNzIucOogdFRRDELIAzoOormAA%3A1701868547024&source=hp&ei=AnRwZdKmPIbR1sQP4YqLqAc&iflsig=AO6bgOgAAAAAZXCCE_PuApA5Oo14KR7Ynu65v6CwG-aC&ved=0ahUKEwjSr8qx8vqCAxWGqJUCHWHFAnUQ4dUDCAk&uact=5&oq=dolar&gs_lp=Egdnd3Mtd2l6IgVkb2xhcjIKECMYgAQYigUYJzIKECMYgAQYigUYJzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMggQABiABBixAzILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMggQABiABBixAzIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBSPUEUABY8QNwAHgAkAEAmAHTAaABiQaqAQUwLjMuMbgBA8gBAPgBAcICDhAAGIAEGIoFGLEDGIMBwgIREC4YgAQYsQMYgwEYxwEY0QPCAgUQABiABMICCBAuGIAEGLED&sclient=gws-wiz", headers=headers)

# print(page.content)

Bs = BeautifulSoup(page.content, 'html.parser')
# span Class = DFlfde SwHCTb
atributos = {'class': 'g'}
# respostas= soup.Find_all("div", class_="g")
valor_dolar = Bs.find_all("span", class_='DFlfde SwHCTb')[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])
