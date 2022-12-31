
#objetivo de este ejercicio es la reutilización de código y los módulos random y math.
import random
import math 

#Incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini, fin y mensaje. 
def leer_numero(ini, fin, mensaje):
    #repetirse hasta que el usuario no lo escriba bien (lo que incluye cualquier valor que no sea un número del ini al fin
    try:
        numero = int(input())
    except TypeError:
        print("ERROR: el número insertado no se encuentra en el rango ini-fin")
    #Leer por pantalla un número >= que ini y <= que fin.    
    if(numero >= ini and numero <= fin):
        return numero
    #A la hora de hacer la lectura se mostrará en el input el mensaje enviado a la función.  
    while True:
        print(mensaje)

#Crear una nueva función llamada generador
#El primer numero será llamado numeros, deberá ser entre 1 y 20
def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
#El segundo número será llamado modo y requerirá un número entre 1 y 3, ambos incluidos
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

#Generar una lista de números aleatorios decimales entre 0 y 100 con tantos números como el usuario haya indicado.
#normalmente usaría random.randint, pero como se pide que los números deben ser decimales, usaré random.uniform

    numeros_aleatorios = []
    for i in range(numeros):
        num_aleat = random.uniform(0,100)

    #Para cada uno de los números, redondearlos en función de lo que el usuario ha especificado en el modo.
    #Posibles modos:

    #[1] Al alza
        if(modo == 1):
            num_redo = math.trunc(num_aleat)+1
    #[2] A la baja
        elif(modo == 2):
            num_redo = math.trunc(num_aleat)
    #[3] Normal (entiendo esto como que el número aleatorio será igual al redondeado (?))
        else:
            num_aleat = num_redo
    #Para cada número muestra durante el redondeo, el número normal y después del redondeo.
        print("El número aleatorio es el", num_aleat, "y el número redondeado es el", num_redo, ".")
    #Finalmente devolver la lista   
        return numeros_aleatorios

if __name__ == "__main__":
    generador()
        



