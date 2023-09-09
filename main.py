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
         
key=str(input("Which button should the login be entered on? "))
key2=str(input("Which button should the password be entered on? "))
key3=str(input("Which button will the link be entered on?(If not necessary, leave an empty line)"))
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
    print("Error the login button is not assigned!")
    eror=input("Restart the script")
if key2=="":
    print("Error the password entry button is not assigned!")
    eror=input("Restart the script")
if key==key2:
    print("Error assigned buttons match!")
    eror=input("Restart the script")
if key3=="":
    auth_log()
    auth_pass()
else:
    auth_link()
    auth_log()
    auth_pass()