from random import randint

def guess_number():
	minimo = int(input("ingresa el minimo de tu rango: "))
	maximo = int(input("ingresa el maximo de tu rango: "))
	puntos = 90
	numero_adivinar = randint(minimo, maximo)
	print (numero_adivinar)
	num = numero_adivinar - 1
	