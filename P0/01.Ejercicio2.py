#cuenta cuantas veces aparece cada nombre en la lista y devuelve un diccionario
def countNames(names):
    counter = dict()
    for name in names:
        if name in counter.keys():
            counter[name] = counter[name] + 1
        else:
            counter[name] = 1

    return counter
#llamamos a la función countNames para que cuente los nombres
cNames = countNames(["pedro", "ana", "javier", "ana", "ana", "ana", "ana", "pablo", "pablo", "pablo", "pablo"])

#como parámetro de entrada recibe un diccionario: dnames
#y devuelve una tupla (maxn, maxc)
#maxn es el nombre más repetido
#maxc es el número de veces que el nombre está repetido
#Dentro de la función maxRepeat hay un for que escribe las keys y las respectivas values del diccionario
#Resultado esperado:
#pedro => 1
#ana => 5
#javier => 1
#pablo => 4
# max(age, key=age.get)
# Para obtener los valores de un diccionario Python se pueden usar el método get(),
# por lo que si se pasa esta función como parámetro las funciones max() y min()
# devolverán los resultados en base a los valores, no las calves
def maxRepeat(dnames):
    maxn = max(dnames, key=dnames.get)
    maxc = dnames[maxn]
    for key, value in dnames.items():
        print(f"{key} => {value}")
    return (maxn, maxc)

#mostramos el resultado de aplicar la función maxRepeat sobre nuestro diccionario cNames
#el nombre más repetido es Ana que aparece tres veces: ('ana', 5)
print(maxRepeat(cNames), 'Es el nombre más repetido')