import pyautogui ##importa rotinas prontas  
import time

pyautogui.alert('O código vai começar') ##botão troboshuts


time.sleep(0.5)
pyautogui.pause = 100 ##Colocando uma pausa de meio segundo para cada comando
pyautogui.press('win') ##Abrir buscador do Windows
time.sleep(2)
pyautogui.write('chrome') ##Digitar chrome
pyautogui.press('enter') ##Apertar Enter

time.sleep(2)

pyautogui.write('https://drive.google.com/drive/my-drive')
time.sleep(2)
pyautogui.press('enter') ##Apertar Enter
time.sleep(3)

pyautogui.hotkey('win','d') ##Digitando combinação de duas teclas, apertando Windows+d

pyautogui.moveTo(1762,19) ##Move o mouse até essa coordenada
pyautogui.mouseDown() ##clicando com o botão esquerdo do mouse, caso queira apertar o direito usar o botão left

pyautogui.moveTo(906, 581) ##Após clicar eu vou arrastar, antes de soltar o botão do mouse, da um alt tab

pyautogui.hotkey('alt','tab')

pyautogui.mouseUp() ##Largar o mouse

time.sleep(3)

pyautogui.alert('O código acabou de rodar, pode usar seu computador novamente')