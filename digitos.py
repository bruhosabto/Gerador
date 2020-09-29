from random import randint
class Digito:

	def __init__(self,valor):
		#nnb0g198
		self.peso = valor
		self.alfa = "abcdefghijlmknopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789_#!/\\=+-*"
		self.tm = len(self.alfa)
		self.a = 0
		self.b = 0
		self.c = 0
		self.d = 0
		self.e = 0
		self.g = 0
		self.h = 0#8
		self.i = 0
		self.j = 0
		self.k = 0
		self.l = 0
		self.m = 0
		self.n = 0
		self.o = 0
		self.p = 0
		self.string = " "
		
	def gerente(self):
		retorno = 0
		if self.peso == 8:
			retorno = self.case_01()
		if self.peso == 9:
			retorno = self.case_02()
		if self.peso == 10:
			retorno = self.case_03()
		if self.peso == 11:
			retorno = self.case_04()
			
		if self.peso == 12:
			retorno = self.case_05()
		if self.peso == 13:
			retorno = self.case_06()
		if self.peso == 14:
			retorno = self.case_07()
		if self.peso == 15:
			retorno = self.case_08()
		if self.peso == 16:
			retorno = self.case_09()
		return retorno
		
	
	
	def case_01(self):#oito digitos
		
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		
		return self.string
	
	def case_02(self):
	
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		
		return self.string
	def case_03(self):
	
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string +=str(lista[j])
		
		return self.string	
	def case_04(self):
	
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		
		return self.string	
	def case_05(self):
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		
		return self.string
	def case_06(self):
	
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		l = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		self.string += str(lista[l])
		
		return self.string
	def case_07(self):
	
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		l = randint(0,self.tm-1)
		m = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		self.string += str(lista[l])
		self.string += str(lista[m])
		
		return self.string
	def case_08(self):
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		l = randint(0,self.tm-1)
		m = randint(0,self.tm-1)
		n = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		self.string += str(lista[l])
		self.string += str(lista[m])
		self.string += str(lista[n])
		
		return self.string
	def case_09(self):
		lista = list(self.alfa)
		a = randint(0,self.tm-1)
		b = randint(0,self.tm-1)
		c = randint(0,self.tm-1)
		d = randint(0,self.tm-1)
		e = randint(0,self.tm-1)
		f = randint(0,self.tm-1)
		g = randint(0,self.tm-1)
		h = randint(0,self.tm-1)
		i = randint(0,self.tm-1)
		j = randint(0,self.tm-1)
		k = randint(0,self.tm-1)
		l = randint(0,self.tm-1)
		m = randint(0,self.tm-1)
		n = randint(0,self.tm-1)
		p = randint(0,self.tm-1)
		
		self.string = str(lista[a])
		self.string += str(lista[b])
		self.string += str(lista[c])
		self.string += str(lista[d])
		self.string += str(lista[e])
		self.string += str(lista[f])
		self.string += str(lista[g])
		self.string += str(lista[h])
		self.string += str(lista[i])
		self.string += str(lista[j])
		self.string += str(lista[k])
		self.string += str(lista[l])
		self.string += str(lista[m])
		self.string += str(lista[n])
		self.string += str(lista[p])
		
		return self.string
