###
#Las listas que no se pueden alterar se llaman: TUPLAS
#Son listas pero que se escriben con ().

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Si solo quiero definir una tupla con un solo elemento es (x,)

#Como hacer un bucle con TUPLAS
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

##Como redefinir una dupla 
#Ejemplo:
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)