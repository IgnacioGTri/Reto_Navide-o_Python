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

print(f"¡Faltan {dias} días para Navidad!")