import pyautogui
import webbrowser
from time import sleep

telefones = []

#Abrir o arquivo txt, importante colocar "r" no código para informar que só vai ler
with open('lista telefone.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n') [0])
        print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1047,244, duration=1)
    sleep(10)
    pyautogui.typewrite('Oi, sou o robo do Leon e agora eu envio msg automatica por aqui hehe!!')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)


