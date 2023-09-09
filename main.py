import keyboard
from config import login, password, link
print("\n███████╗███╗░░░███╗██╗░░░░░"
         "\n██╔════╝████╗░█l███║██║░░░░░"
         "\n█████╗░░██╔████╔██║██║░░░░░"
         "\n██╔══╝░░██║╚██╔╝██║██║░░░░░"
         "\n██║░░░░░██║░╚═╝░██║███████╗"
         "\n╚═╝░░░░░╚═╝░░░░░╚═╝╚══════╝"
         "\nautoauth by fonnto v 0.2(alpha version)"
         )
         
key=str(input("На какую кнопку должен вводиться логин? "))
key2=str(input("На какую кнопку должен вводиться пароль? "))
key3=str(input("На какую кнопку введеться ссылка?(Если не нужно оставь пустую строку)"))
def auth_log():
    for i in range(1):
        keyboard.wait(key)
        keyboard.send("backspace")
        keyboard.write(login)
        i=1
def auth_pass():
    for i in range(1):
        keyboard.wait(key2)
        keyboard.send("backspace")
        keyboard.write(password)
def auth_link():
    for i in range(1):
        keyboard.wait(key3)
        keyboard.send("backspace")
        keyboard.write(link)
if key=="":
    print("Ошибка кнопка ввода логина не назначена!")
    eror=input("Перезапустите скрипт")
if key2=="":
    print("Ошибка кнопка ввода пароля не назначена!")
    eror=input("Перезапустите скрипт")
if key==key2:
    print("Ошибка назначеные кнопки совпадают!")
    eror=input("Перезапустите скрипт")
if key3=="":
    auth_log()
    auth_pass()
else:
    auth_link()
    auth_log()
    auth_pass()