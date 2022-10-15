# Escribe aquí tu código
def gcd(x, y):
    enteromayor = max(x, y)
    enteromenor = min(x, y)
    #condición de parada
    if enteromayor - enteromenor == 0:
        return x
    z = enteromayor - enteromenor

    #llamada recursiva
    return gcd(enteromenor, z)

#casos de prueba
print(gcd(270,192)) # 6

print(gcd(9, 6)) # 3

print(gcd(30, 75)) # 15