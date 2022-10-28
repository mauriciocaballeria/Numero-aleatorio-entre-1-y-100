import random

numero_aleatorio = random.randint(1,100)

nombre = input("Ingresa tu nombre:  ")
print("Debes adivinar el numero entre 1 y 100")
x=int(input("Ingresa el numero que crees que es (0 para parar): \n "))
cuenta = 1 

while numero_aleatorio != x and x>0:
    cuenta = cuenta + 1
    dif = abs(x - numero_aleatorio)
    if dif<=5:
        print("Sorry "+nombre+", ese no es pero estas a una distancia menor a 5\n")
    else:
        if dif<=10:
            print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 5 y menor a 10\n")
        else:
            if dif<=20:
                print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 10 y menor a 20\n")
            else:
                print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 20\n")
                            
    numero_aleatorio = random.randint(1,100)
    x=int(input("Ingresa el numero que crees que es (0 para parar): \n "))
if x==0:
    print("No lo lograste "+nombre+" a pesar de tratar "+str(cuenta)+" veces. Mas suerte para otra vez !!")
else:
    print("Felicitaciones "+nombre+" lo lograste en "+str(cuenta)+" intentos")
