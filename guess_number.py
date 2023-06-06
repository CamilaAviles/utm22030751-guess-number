from random import randint

def guess_number():
	minimo = int(input("ingresa el minimo de tu rango: ")) #Se le pide al usuario ingresar su rango minimo
	maximo = int(input("ingresa el maximo de tu rango: ")) #Se le pide al usuario ingresar su rango maximo
	puntos = 90 # se dice que puntos es igual a 90
	numero_adivinar = randint(minimo, maximo) # se crea un numero random entre el rango minimo y maximo ingresado por el usuario
	print (numero_adivinar) # se imprime el numero creado random
	num = numero_adivinar - 1 # se le resta 1 al numero
	while num!=numero_adivinar and puntos>0:
		print(f"Adivina el numero entre: {minimo} y {maximo}: ")
		num = int(input())
		if num>numero_adivinar: # si el numero es mayor al numero adivinar entonces:
			print("Muy alto") # imprimir que es muy alto
			puntos = puntos-10	# por cada intento fallido se le restan 10 puntos
			print("le quedad ",puntos," puntos") # se imprime los puntos que le quedan
		elif num<numero_adivinar: # si el numero es menos al numero adivina entonces:
			print("Muy bajo") # imprimir que es muy bajo
			puntos = puntos-10	
			print("le quedad ",puntos," puntos")

	if puntos==0: # si se acaban los puntos entonces:
		print("Game Over") # imprime game over
	else:
		print("exacto, les restaron", puntos,"puntos, eres un genio!") # si adivino, entonces imprime los puntos restantes

	