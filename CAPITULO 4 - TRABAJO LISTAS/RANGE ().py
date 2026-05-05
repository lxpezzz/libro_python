#Señalizar el rango de valores

for value in range(1, 11):
    print(value)


#como poner un listado de numeros
numeros = list(range(1, 6))
print(numeros)

#poner un listado de pares
pares = list(range(2, 11, 2))
print(pares)

###Numeros cuadreados 
cuadrados = []
for value in range(1, 11):
    cuadrado = value ** 2
    cuadrados.append(cuadrado)
print(cuadrados)

#de forma más simple: 
cuadrados = []
for value in range(1, 11):
    cuadrados.append(value**2)
print(cuadrados)

##COMO ENSEÑAR EL NUMERO MIN, MAX Y LA SUMA DE DIGITOS
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

##Como escribirlo de forma más pro

cuadrados = [value**2 for value in range(1, 11)]
print(cuadrados)