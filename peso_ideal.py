# Preguntamos por el nombre y lo guardamos en la variable Nombre
Nombre = input("¿Cómo te llamas?")
# Preguntamos por el sexo y guardamos el valor h o m en la variable Sexo
Sexo = input("¿Eres hombre(h) o mujer(m)?")
# Saludamos por cortesía
print(f" Hola buenos días {Nombre} ,un gusto saludarte.")
# Explicamos al usuario lo que vamos ha hacer
print("Hoy vamos va calcular tu peso ideal y te vamos a decir lo cerca que estas de conseguirlo. Buena suerte!!!")
# Preguntamos por el peso en kg y guardamos el valor en la variable peso_real
peso_real = float(input("Digame su peso en kg: "))
# Preguntamos por la altura en centimetros y guardamos el valor en la variable altura
altura = float(input("Digame su altura en cm: "))
# Definimos la función peso ideal dependiendo de si es hombre o mujer
def peso_ideal (a):
    if Sexo == "h": 
        z=float(50+((a-150)*75)/100)
        return z
    else: 
        z=float(50+((a-150)*60)/100)
        return z
# Fin de la deficincion de la funcion
# Mostramos el peso ideal en Kilogramos
print(f"{Nombre}, tu peso ideal es: {peso_ideal(altura)} Kg")
# Definimos la variable Sobrepeso para comparar con el peso ideal 
Soprepeso = float(peso_real - peso_ideal(altura))
# Si su peso sobrepasa el peso ideal le decimos que se cuide y si no le decimos que tiene que alimentarse un poco mas
if Soprepeso > 0:
    print(f"{Nombre}, estas {Soprepeso} Kg por encima de tu peso ideal")
    print("Deberías hacer más ejercicio")
elif Soprepeso == 0:
    print(f"{Nombre}, estas en tu peso ideal. Enhorabuena!!!")
else:    
    print(f"{Nombre}, estas {Soprepeso} Kg por debajo de tu peso ideal")
    print("Deberías comer un poco más")
# Finalizamos el programa
print("Fin del programa")
