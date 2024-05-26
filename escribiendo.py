import pyautogui
import pygetwindow as gw
import time

def escribir(mensaje):
    window_title = 'Edge'
        # Encuentra la ventana del juego por su título
    game_window = gw.getWindowsWithTitle(window_title)
        # Activa la ventana del juego y lleva el foco a la ventana
    if len(game_window) > 0:
        game_window[0].activate()
        time.sleep(0.5)    # Espera un breve momento para que la ventana tenga el focus
    else:
        print(f"No se pudo encontrar la ventana del juego con el título '{window_title}'.")
    #Escribiendo cuestion
    for char in mensaje:
        pyautogui.keyDown(char)
        pyautogui.keyUp(char)
escribir('Escribir comando aqui')