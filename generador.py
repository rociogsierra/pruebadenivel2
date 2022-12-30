
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

