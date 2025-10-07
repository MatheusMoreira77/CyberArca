from Database import Conexao, adicionar, Copy_password, Editar, Deletar
import os
import time

clean = os.system('cls' if os.name == 'nt' else 'clear')
Conexao()
while True:
    clean = os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------------------")
    print("         Welcome to Ark Password Manager        ")
    print("------------------------------------------------")


    print("1 - Add Login")
    print("2 - Copy Password")
    print("3 - Edit Logins")
    print("4 - Delete Login")
    print("5 - Exit")

    input_user = input("Choose an option: ")
    match input_user:
        case '1':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                  Add Login                     ")
            print("------------------------------------------------")
            adicionar()
            time.sleep(2)
            clean = os.system('cls' if os.name == 'nt' else 'clear')
        case '2':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                Copy Password                   ")
            print("------------------------------------------------")
            Copy_password()
            time.sleep(2)
            clean = os.system('cls' if os.name == 'nt' else 'clear')
        case '3':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                Edit Logins                     ")
            print("------------------------------------------------")
            Editar()
            time.sleep(2)
            clean = os.system('cls' if os.name == 'nt' else 'clear')
        
        case '4':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                Delete Login                    ")
            print("------------------------------------------------")
            Deletar()
            clean = os.system('cls' if os.name == 'nt' else 'clear')
        case '5':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                Exiting...                      ")
            print("------------------------------------------------")
            time.sleep(2)
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            break
        case _:
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid option. Please try again.")
            time.sleep(2)
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            continue
        