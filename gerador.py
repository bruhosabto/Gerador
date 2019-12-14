#!/usr/bin env python


 # gerador
 # autor_brunosantos
 
 
 
from random import randint
import sys
 
 
 
class Numeros:
	def __init__(self,primeiro):
	
		self.primeiro = primeiro
		self.anterior = 0
		self.tm = 0
		
	def Gerar(self):
	
		self.anterior = self.primeiro
		self.tm = len(str(self.anterior))
		if self.tm  <= 8:
			self.primeiro=self.anterior+1
		else: 
			self.primeiro = -1
			
		return self.primeiro
		
		


class Letras:
	def __init__(self,alfa,limite):
	
		 self.alfa = alfa # recebe o alfabeto
		 self.limite = limite # tamanho da string a ser gerada
		 self.tm = len(self.alfa) - 1
		 self.contador = 0
		 
		 
	def String(self):
		self.lista = list(self.alfa)
		self.string =  ""
		self.random = 0
		
		for c in range(0,self.limite):
		
			self.random = randint(0,self.tm)
			self.string += str(self.lista[self.random])
			
		return self.string
 
def numeros(x):
 	N = Numeros(x)
	cont = 0
	while True:
		
		if cont == -1:
			break
		else:
	 		print cont
	 	cont = N.Gerar()
 	


def string(alfa,x,y):
	S = Letras(alfa,y)
	
	cont = 0
	
	while cont < x:
		
		print S.String()
		cont += 1


def main():
	
	
	try:
		alfa = sys.argv[1]
		quant = sys.argv[2]
		tm = sys.argv[3]
		numero = sys.argv[4]
		quant = int(quant)
		tm = int(tm)
		numero = int(numero)
		
		
	except:
		alfa = "abcdefghijklmnopqrstuvxywz"
		quant = 2000
		tm = 8
		numero = 81000000
		
		#numeros(numero)
        string(alfa,quant,tm)	
        numeros(numero)
	
main()
