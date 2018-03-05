"""
@author: Saul Mamani
@email: luas0_1@yahoo.es
@web: saulmamani.github.io
@phone: +591 76137269
"""

import random
import os

class TresRaya:
	M = []	
	
	def __init__ (self):
		self.M = [[0,0,0],[0,0,0],[0,0,0]]

	def __mostrar(self):
		for i in self.M:
			for j in i:
				if j == 0:
					print "_\t",
				elif j == 1:
					print "X\t",
				else:
					print "0\t",
			print

	def jugarPersona(self):
		i = input("Ingrese Fila: ")
		j = input("Ingrese Columna: ")
		if i > 2 or j > 2:
			print "-----Fuera de Rango, elija otra!!!"
			self.jugarPersona()
		elif self.M[i][j] == 0:
			self.M[i][j] = 1
		else:
			print "-----Esa posicion ya esta ocupada, elige otra!!!"
			self.jugarPersona()	

	def jugarMaquina(self):
		i = random.randint(0, 2)
		j = random.randint(0, 2)
		if self.M[i][j] == 0:
			self.M[i][j] = -1
		else:
			self.jugarMaquina()

	def verificarEmpate(self):
		listaAux = []
		listaAux.extend(self.M[0])
		listaAux.extend(self.M[1])
		listaAux.extend(self.M[2])
		return listaAux.count(0)

	def contarFila(selft, M, dato):
		return M[0].count(dato) == 3 or M[1].count(dato) == 3 or M[2].count(dato) == 3

	def mapearFilaColum(self, a, b, c):
		x = []
		x.append(a)
		x.append(b)
		x.append(c)
		return x

	def verificarGanador(self):
		ganaPersona = False
		ganaMaquina = False

		#verificando ganadores filas
		ganaPersona = self.contarFila(self.M, 1)
		ganaMaquina = self.contarFila(self.M, -1)

		if ganaPersona:
			print "Felicidades!!! Ganaste"
			return True
		if ganaMaquina:
			print "Perdiste!!! =("
			return True
		
		#verificando columnas
		matrizAux = map(self.mapearFilaColum, self.M[0], self.M[1], self.M[2])

		ganaPersona = self.contarFila(matrizAux, 1)
		ganaMaquina = self.contarFila(matrizAux, -1)

		if ganaPersona:
			print "Felicidades!!! Ganaste"
			return True
		if ganaMaquina:
			print "Perdiste!!! =("
			return True

		#verificando diagonales
		matrizAux = []
		listaCol = []
		for i in xrange(0,3):
			listaCol.append(self.M[i][i])
		matrizAux.append(listaCol)
		
		listaCol = []
		for i in xrange(0,3):
			listaCol.append(self.M[i][2-i]) 
		matrizAux.append(listaCol)

		ganaPersona = matrizAux[0].count(1) == 3 or matrizAux[1].count(1) == 3
		ganaMaquina = matrizAux[0].count(-1) == 3 or matrizAux[1].count(-1) == 3

		if ganaPersona:
			print "Felicidades!!! Ganaste"
			return True
		if ganaMaquina:
			print "Perdiste!!! =("
			return True

		#verificar empate
		if self.verificarEmpate() == 0:
			print "Empate!!!!!"
			return True

		return False

	def jugar(self):
		op = 0
		while True:
			os.system('clear')
			self.__mostrar()
			
			if op % 2 == 0:
				self.jugarPersona()
			else:
				self.jugarMaquina()

			op+=1

			if self.verificarGanador():
				break

		print "======= RESULTADO FINAL ======="
		self.__mostrar()