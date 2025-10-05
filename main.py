from Database import Conexao, adcionar, Copy_password
import os

clean = os.system('cls' if os.name == 'nt' else 'clear')
Conexao()

print("------------------------------------------------")
print("         Welcome to Ark Password Manager        ")
print("------------------------------------------------")

while True:
    print("1 - Add Login")
    print("2 - Edit Login")
    print("3 - Delete Login")
    print("4 - Copy Password")

    input_user = input("Choose an option: ")
    match input_user:
        case '1':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("                  Add Login                     ")
            print("------------------------------------------------")
            adcionar()
            break
        case '2':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("         Edit Login         ")
            print("------------------------------------------------")
            Copy_password()
            break
        case '3':
            clean = os.system('cls' if os.name == 'nt' else 'clear')
            print("------------------------------------------------")
            print("         Delete Login         ")
            print("------------------------------------------------")