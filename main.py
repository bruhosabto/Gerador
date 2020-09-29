
from digitos import Digito
from random import randint






def main(nome,quantidade):
	
	criar = open(nome,"a+")
	contador = 0
	while contador < quantidade:
		
		contador += 1
		a = randint(8,16)
		gere = Digito(a)
		
		criar.write(gere.gerente()+str("\n"))
		print gere.gerente()+"\n"
		


nome = raw_input("informe o nome para o arquivo de saida:")
quantidade = input("informe a quantidade senhas:")

main(nome,quantidade)
