##
#El bucle for se utiliza para crear listas. Estructura: 
# For ...... in ......:  


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#Enviar un mensaje a cada mago: 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"\n{magician.title()}, eres un fantástico mago.")

print("\nINVITACIÓN")
print("Te invito a mi fiesta para que hagas algun truco de magia.")