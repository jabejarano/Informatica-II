#Ejercicio 0.1: Calcular año bisiesto
#La función devolverá un True si el año ES Bisiesto
#y un False si el año NO es Bisiesto

def esBisiesto(number):
    if number % 4 == 0 and number % 100 != 0 or number % 400 == 0:
        return True
    else:
        return False
#Escribe aquí abajo el año que quieres comprobar si es bisiesto
print(esBisiesto(2020))