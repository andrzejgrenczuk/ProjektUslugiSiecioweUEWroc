import login
from menu import menu,menu_adm

print("================================================================")
print("| System wprowadzania i odgadywania zwierząt                   |")
print("|                                                              |")
print("| Projekt zaliczeniowỵ̣̣                                         |")
print("----------------------------------------------------------------")
print("| Autorzy: Mikołaj Szaga, Piotr Urban, Andrzej Greńczuk       |")
print("================================================================")

mail = input("Proszę podać swój adres email: ")
pwd = input("Prosze podać hasło: ")
login.login(mail,pwd)
if mail != "root@local":
    while True:
        menu()
else:
    while True:
        menu_adm()

