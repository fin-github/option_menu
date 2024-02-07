from pydirectinput import keyDown, keyUp
from os import system as cmd

def hi():
    print("hi")
def leave():
    cmd("cls")
    print("Bye!")
    keyDown("ctrl")
    keyDown("c")
    keyUp("ctrl")
    keyUp("c")
