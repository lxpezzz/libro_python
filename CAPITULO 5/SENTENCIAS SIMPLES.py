####
# Sentencias Simples:
# if prueba_condicional:
# Hacer algo
age = 19
if age >= 18:
    print("\nEres mayor de edad!")

# Se puede poner todas las líneas de código que se quiera. Mientras que las
# salidas están sangradas.
age = 19
if age >= 18:
    print("\nEres mayor de edad!")
    print("\nTienes que votar este año.")

###
# SENTECIAS IF-ELSE
# Se crea un condicional con IF, luego se ejecuta si se lanza la orden. Sino se
# ejecuta el ELSE.
age = 17
if age >= 18:
    print("\Puedes ir a votar.")
else:
    print("\nNo puedes votar.")

## SENTENCIAS IF-ELIF-ELSE
age = 12
if age < 4:
    print("\nYour admission cost is 0€.")
elif age < 18:
    print("\nYour admission cost is 20€.")
else:
    print("\nYour admission cost is 40€.")

##UTILIZAR MÚLTIPLES BLOQUES ELIF
age = 21
if age < 4:
    print("\nYour admission cost is 0€.")
elif age < 18:
    print("\nYour admission cost is 20€.")
elif age < 25:
    print("\nYour admission cost is 30€.")
else:
    print("\nYour admission cost is 40€.")
