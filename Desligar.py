import pyautogui
import time
import datetime
from pynput.keyboard import Controller, Key

keyboard = Controller()

def horario(acao, hora):
    hora = datetime.datetime.strptime(hora, '%H:%M').time()
    print(f"esperando ate {hora}")

    while True:
        hora_atual = datetime.datetime.now().time()

        if hora_atual >= hora:
            print(f"Hora alcançada: {hora}")
            acao()
            break
        time.sleep(1)

def desligar():
    pyautogui.PAUSE = 1.5
    pyautogui.press("win")
    pyautogui.press("tab")
    time.sleep(1)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep
    keyboard.press(Key.down)
    pyautogui.press("enter")
    keyboard.press(Key.down)
    pyautogui.press("enter")
    

def hibernar():
    pyautogui.PAUSE = 1.5
    pyautogui.press("win")
    pyautogui.press("tab")
    time.sleep(1)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.down)
    time.sleep
    keyboard.press(Key.down)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")

if __name__ == "__main__":
    user_time = input("Digite horario HH:MM:  ")
    escolha = input("Desligar(1)\nHibernar(2)")
    

    if escolha == "1":
        acao = desligar
    elif escolha == "2":
        acao = hibernar
    else:
        print("Escolha invalida")
    horario(acao, user_time)