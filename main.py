from digitos import Digito
from random import randint

def main(nome, quantidade):
    # Opens the file in append mode
    with open(nome, "a+") as criar:
        for _ in range(quantidade):
            # Generates a random weight value between 8 and 16
            a = randint(8, 16)
            # Instantiates the Digito class with the generated weight
            gere = Digito(a)
            # Generates the password and writes it to the file
            senha = gere.gerente()
            criar.write(senha + "\n")
        print("[!] Done")

# Requests the output file name and the number of passwords
nome = input("Type the output file name: ")
quantidade = int(input("Enter the number of passwords: "))

main(nome, quantidade)
