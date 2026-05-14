##
# Hacer comparaciones y que sean True or False
# Prubas de igualdad y desigualdad:
marcas = ["nike", "adidas", "quechua", "new balance"]
for marca in marcas:
    if marca == "nike":
        print("\nMi marca de zapatillas es Nike.")
    else:
        print(f"\nNo me gustan tanto las zapatillas {marca.title()}.")

if "gucci" not in marcas:
    print("\nMe quiero comprar las Gucci que me faltan.")
if marcas != "gucci":
    print("\nMe quiero comprar las Gucci que me faltan.")

###
# Comparaciones de Mayúsculas o minúsculas
# método lower()
marca = "Nike"

print("\n¿marca == 'nike'? Predicción: False")
print(marca == "nike")

print("\n¿marca.lower() == 'nike'? Predicción: True")
print(marca.lower() == "nike")

###
# COMPARACIONES NÚMERICAS:
edad = 24

print("\n¿edad == 24? Predicción: True")
print(edad == 24)

print("\n¿edad != 18? Predicción: True")
print(edad != 18)

print("\n¿edad > 18? Predicción: True")
print(edad > 18)

print("\n¿edad < 18? Predicción: False")
print(edad < 18)

print("\n¿edad >= 24? Predicción: True")
print(edad >= 24)

print("\n¿edad <= 20? Predicción: False")
print(edad <= 20)

print("\n¿edad <= 20? Predicción: False")
print(edad <= 20)

##PRUEBAS CON AND Y OR
dinero = 100

print("\n¿edad >= 18 and dinero >= 50? Predicción: True")
print(edad >= 18 and dinero >= 50)

print("\n¿edad >= 18 and dinero >= 200? Predicción: False")
print(edad >= 18 and dinero >= 200)

print("\n¿edad >= 25 and dinero >= 10? Predicción: False")
print(edad >= 25 and dinero >= 10)

print("\n¿edad >= 18 or dinero >= 200? Predicción: True")
print(edad >= 18 or dinero >= 200)

# PRUEBA PARA COMPROBAR SI UN ELEMENTO ESTÁ EN UNA LISTA.

marcas = ["nike", "adidas", "quechua", "new balance"]

print("\n¿'nike' está en marcas? Predicción: True")
print("nike" in marcas)

print("\n¿'adidas' no está en marcas? Predicción: False")
print("adidas" not in marcas)

print("\n¿'gucci' está en marcas? Predicción: False")
print("gucci" in marcas)

print("\n¿'gucci' no está en marcas? Predicción: True")
print("gucci" not in marcas)
