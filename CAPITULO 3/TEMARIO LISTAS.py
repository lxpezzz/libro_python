###
#Ejemplo de como cambiar un elemento de una lista, y modificarla en texto
###

marcas = ['BMW', 'AUDI', 'TOYOTA', 'HONDA']

marcas[0] = 'Reanult'
mensaje1 = f"Tengo un coche de la marca {marcas[0]}"
print(marcas)
print(mensaje1)


###
#Como añadir nuevos elementos a las listas.
###
marcas.append('Kia')
print(marcas)

###
#Como añadir elementos a una lista sin tener ningun dato al principio
###

nombres = []
nombres.append('Héctor')
nombres.append('Nerea')
nombres.append('Ana')
nombres.append('Alfredo')

print(nombres)


###
#Añadir una palabra a la lista sin tener que modificar nada. comando insert
###

familia = ['Héctor', 'Nerea', 'Ana', 'Alfredo']
familia.insert(1, 'Irene')
print(familia)


###
#Elimina un elemento de la lista. Comando del
###

del familia[0]
print(familia)


###
#Eliminar un elemento con el método pop()
###

marcas = ['BMW', 'AUDI', 'TOYOTA', 'HONDA']
popped_marcas = marcas.pop()
print(popped_marcas)
print(marcas)

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
ultimo_mes = meses.pop()
print(f"El último mes del año es {ultimo_mes.title()}")

##
#Como eliminar un elemento concreto de la lista. 
##
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
print(meses)

meses.remove('junio')
print(meses)
