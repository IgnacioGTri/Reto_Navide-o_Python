#Lista de deseos (wishlist.txt).
#El programa debe permitir al usuario introducir varios deseos navideños.
#El usuario escribe uno a uno los deseos y el programa los va guardando
#en una lista de Python. Cuando el usuario escriba la palabra “fin”, el
#programa debe detener la entrada.
#El programa debe de mostrar el número total de deseos introducidos
#ordenados alfabéticamente.

listaDeseos = []

while True:
    deseo = input("Pide tus deseos naviñedos hasta decir 'FIN': ")
    
    if deseo.lower() == "fin":
        break
    
    listaDeseos.append(deseo.lower())
    
listaDeseos.sort()

print("\nLista de Deseos Ordenada:")
for elemento in listaDeseos:
    print("-", elemento)