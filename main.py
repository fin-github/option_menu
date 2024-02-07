from keyboard import add_hotkey
from pydirectinput import keyUp
from classes import Option
from functions import hi as hi_func, leave
from time import sleep as wait
from os import system as cmd
selected = 0
options = [
    Option("Example 1", "bhvghvcfg", hi_func),
    Option("Example 2", "This is Example 2", hi_func),
    Option("Example 3", "This is Example 3", hi_func),
    Option("Example 4", "This is Example 4", hi_func)
]
activeops = []

options.append(Option("Exit", "Exit the menu", leave))
def clr(): cmd("cls")
def spaces(amt:int):
    tmp=''
    for i in range(0,amt): tmp+=' '
    return tmp

def handle_up():
    global selected
    if selected == 0:
        selected = len(options)-1
    else:
        selected -=1
    render_options()
def handle_down():
    global selected
    if selected == len(options)-1:
        selected=0
    else:
        selected +=1
    render_options()
def handle_enter():
    isactive = True if options[selected] in activeops else False
    if isactive: 
        activeops.remove(options[selected])
    else:
        activeops.append(options[selected])
    render_options()




def render_options():
    clr()
    i=0
    for option in options:
        print(f"{option.name}{spaces(15 - len(option.name))}{'+' if option in activeops else 'x'}{spaces(7)}{'0' if i == selected else ''}")
        i+=1
    print(f"\n{options[selected].desc}")
    print(f"\n\nDEBUG: I={i}|||sel={selected}||lenops={len(options)}||lenops(i)={len(options)-1}||activeops={activeops}")
    for op in activeops:
        op.function()

render_options()
add_hotkey("up", handle_up)
add_hotkey("down", handle_down)
add_hotkey("enter", handle_enter)

try:
    wait(999)
except KeyboardInterrupt:
    keyUp("ctrl")
    exit()
print("Timeout...")
