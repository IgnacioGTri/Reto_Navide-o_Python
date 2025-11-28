#Saludo navideño personalizado. 
#El programa debe pedir al usuario se nombre, mostrar un saludo navideño 
#festivo que incluya el nombre y la fecha actual.
import datetime

saludo= input("Escribe tu nombre: ")
print(f"¡¡Feliz Navidad, {saludo}!! La fecha de hoy es: {datetime.date.today()}")


#Cuenta atrás hasta Navidad.
#El programa debe de calcular cuántos días faltan para el 25 de diciembre 
#del año actual. Si ya ha pasado Navidad, debe calcular los días hasta la 
#próxima Navidad del año siguiente.
import datetime

fecha = datetime.date.today()
actual = fecha.year
navidad=datetime.date(actual, 12, 25)

if fecha > navidad: 
    navidad= datetime.date(actual+1, 12, 25)

dias = (navidad - fecha).days

print(f"¡Faltan {dias} días para Navidad!\n")

#Menú de villancicos. 
#Se debe de mostrar un menú con varias opciones de villancicos.  
#El usuario elige una opción y el programa muestra la letra del villancico. 
#El menú debe repetirse hasta que el usuario elija “SALIR”
while True:
    print("\nMenú de Villancicos")
    print("1. Campanas de Belén")
    print("2. Hacia Belén va una Burra")
    print("3. Los Peces en el Río")
    print("4. Mi Burrito Sabanero")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        with open("campanas.txt", "r", encoding="utf-8") as archivo:
            print("\n" + archivo.read())

    elif opcion == "2":
        with open("burra.txt", "r", encoding="utf-8") as archivo:
            print("\n" + archivo.read())

    elif opcion == "3":
        with open("peces.txt", "r", encoding="utf-8") as archivo:
            print("\n" + archivo.read())

    elif opcion == "4":
        with open("sabanero.txt", "r", encoding="utf-8") as archivo:
            print("\n" + archivo.read())

    elif opcion == "5":
        print("¡Se acabó los Villancicos!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")