from digitos import Digito
from random import randint

def main(nome, quantidade):
    # Abre o arquivo em modo de escrita
    with open(nome, "a+") as criar:
        for _ in range(quantidade):
            # Gera um valor aleatório de peso entre 8 e 16
            a = randint(8, 16)
            # Instancia a classe Digito com o peso gerado
            gere = Digito(a)
            # Gera a senha e grava no arquivo
            senha = gere.gerente()
            criar.write(senha + "\n")
            print(senha)

# Solicita o nome do arquivo e a quantidade de senhas
nome = input("Informe o nome para o arquivo de saída: ")
quantidade = int(input("Informe a quantidade de senhas: "))

main(nome, quantidade)
