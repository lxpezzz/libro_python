'''
## Guardar las funciones en módulos
# Importar un módulo completo
# Todas la funciones de módulo estarán disponibles a través de:
# # nombre_módulo.nombre_funcion()
'''

'''
### Importar funciones específicas
# Se puede importar una función esepecífica desde un módulo.
# La sintaxis:
### from nombre_modulo import nombre_funcion
# Se puede importar tantas funciones como queramos
### from nombre_modulo import funcion_0, funcion_1, funcion_2
'''

'''
# Usar as para dar un alias a una función
# Si el nombre de una función que vamos a importar puede generar un conflicto
# con un nombre ya creado en el programa, podemos usar un alias con un nombre
# alternativo, la estructura es así: 
from nombre_modulo import nombre_funcion as nf
'''
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', ' green peppers', 'extra cheese')

'''
Se puede usar un as para dar un alias a un módulo
La sintaxis es: import nombre_modulo as nm
'''##
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
Importar todas la funciones de un módulo
La sintaxis es: from nombre_modulo import *
'''
from pizza import * 
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

## Dar estilo a las funciones:
# def nombre _funcion(parametro_0, parametro_1='valor predeterminado)
# nombre_funcion(valor_0, parametro_1='valor')

