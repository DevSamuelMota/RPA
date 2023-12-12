# -*- coding: utf-8 -*-
import pyautogui
import time

# Automação Teclado
# Clica apenas uma única vez no alt
pyautogui.keyDown('alt')
# Pressiona a tecla tab
pyautogui.press(['tab'])
# Retira o clique da tecla alt, como quando tiramos o dedo da tecla
pyautogui.keyUp('alt')

# Inicializa a variável procurar com o valor "sim".
# Essa variável é usada como uma condição de controle para o loop while.
# Inicia um loop while que continua enquanto a variável procurar é igual a "sim".
# Este loop será repetido até que a variável procurar seja alterada para "não" dentro do bloco try.
procurarImg = "sim"

while procurarImg == "sim":
    try:
        img = pyautogui.locateCenterOnScreen(
            'Wathsapp.png', confidence=0.7)
        pyautogui.click(img.x, img.y, duration=2)
        procurarImg = 'não'
    except:
        time.sleep(3)
        print("Não foi encontrado")
img = pyautogui.locateCenterOnScreen(
    'Ir.PNG', confidence=0.7)
pyautogui.click(img.x, img.y, duration=2)
pyautogui.write("Kingston marca muito boa.", interval=0.15)
pyautogui.press(['enter'])
