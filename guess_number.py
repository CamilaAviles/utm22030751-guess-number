from random import randint

def guess_number():
	minimo = int(input("ingresa el minimo de tu rango: "))
	maximo = int(input("ingresa el maximo de tu rango: "))
	puntos = 90
	numero_adivinar = randint(minimo, maximo)
	print (numero_adivinar)
	num = numero_adivinar - 1
	while num!=numero_adivinar and puntos>0:
		print(f"Adivina el numero entre: {minimo} y {maximo}: ")
		num = int(input())
		if num>numero_adivinar:
			print("Muy alto")
			puntos = puntos-10	
			print("le quedad ",puntos," puntos")
		elif num<numero_adivinar:
			print("Muy bajo")
			puntos = puntos-10	
			print("le quedad ",puntos," puntos")

	if puntos==0:
		print("Game Over")
	else:
		print("exacto, les restaron", puntos,"puntos, eres un genio!")

	