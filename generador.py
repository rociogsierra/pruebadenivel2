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



