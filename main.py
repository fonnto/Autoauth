import keyboard
from config import login, password
print("\n███████╗███╗░░░███╗██╗░░░░░"
         "\n██╔════╝████╗░█l███║██║░░░░░"
         "\n█████╗░░██╔████╔██║██║░░░░░"
         "\n██╔══╝░░██║╚██╔╝██║██║░░░░░"
         "\n██║░░░░░██║░╚═╝░██║███████╗"
         "\n╚═╝░░░░░╚═╝░░░░░╚═╝╚══════╝"
         "\nauth to ts3.lu by fonnto v 0.1(pre alpha version)"
         )
         
sett=str(input("На какую кнопку должен вводиться логин? "))
sett2=str(input("На какую кнопку должен вводиться пароль? "))
def auth_log():
    for i in range(1):
        keyboard.wait(sett)
        keyboard.send("backspace")
        keyboard.write(login)
        i=1
def auth_pass():
    for i in range(1):
        keyboard.wait(sett2)
        keyboard.send("backspace")
        keyboard.write(password)
       
print("Скрипт работает! Нажми на клавиши которые выбрал!")
auth_log()
auth_pass()
