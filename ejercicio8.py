
#Desarrollar un algoritmo que permita cargar 1000 número enteros generados de manera aleatoria

class NodoArbol:
    def __int__(self, data):
        self.izq = None
        self.der = None
        self.data = data
        self.altura = 0

#Realizar los barridos inorden, preorden, postorden 
#INORDEN
def inorden(raiz):
    if (raiz is not None):
        inorden(raiz.izq)
        print(raiz.data)
        inorden(raiz.der)
#PREORDEN
def preorden(raiz):
    print(raiz.data)
    preorden(raiz.izq)
    preorden(raiz.der)
#POSTORDEN
def postorden(raiz):
    postorden(raiz.der)
    print(raiz.data)
    postorden(raiz.izq)
#POR NIVEL
def por_nivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)
    while(not cola_vacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.data)
        if(nodo.izq is not None):
            arribo(pendientes, nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)

#Determinar si un número está cargado en el árbol
def buscar(raiz, clave):
    pos = None
    if(raiz is not None):
        if(raiz.data == clave):
            pos = raiz
        elif clave < raiz.data:
            pos = buscar(raiz.izq, clave)
        else:
            pos = buscar(raiz.der, clave)
    return pos

#Eliminar 3 elementos del árbol
#ELIMINO EL PRIMER ELEMENTO
def eliminar_nodo(raiz, clave):
    x = None
    if (raiz is not None):
        if (clave < raiz.data):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.data):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.data
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.data = aux.data   
#AHORA ELIMINO EL SEGUNDO ELEMENTO
def eliminar_nodo(raiz, clave):
    y = None
    if (raiz is not None):
        if (clave < raiz.data):
            raiz.izq, y = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.data):
            raiz.der, y = eliminar_nodo(raiz.der, clave)
        else:
            y = raiz.data
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.data = aux.data  
#AHORA ELIMINO EL TERCER ELEMENTO
def eliminar_nodo(raiz, clave):
    z = None
    if (raiz is not None):
        if (clave < raiz.data):
            raiz.izq, z = eliminar_nodo(raiz.izq, clave)
        elif (clave > raiz.data):
            raiz.der, z = eliminar_nodo(raiz.der, clave)
        else:
            z = raiz.data
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.data = aux.data  

#Determinar la altura del subárbol izquierdo y del subárbol derecho
def altura(raiz):
    if(raiz is None):
        return -1
    else:
        return raiz.altura 

def actualizaraltura(raiz):
    if(raiz is not None):
        alt.izq = altura(raiz.izq)
        alt.der = altura(raiz.der)
        raiz.altura = (alt.izq if alt.izq > alt.der else alt.der) + 1

#Contar cuántos números pares e imapares hay en el árbol
#VERIFICAR PRIMERO SI EL NUMERO ES PAR O IMPAR
def par(num):
    if(num % 2 == 0):
        return False
    else:
        return True

#GENERO EL ÁRBOL DE 0 A 1000
import random
rango = 1000
num_aleatorio = random.randint(0, 1000)
arbol = NodoArbol(num_aleatorio)
#CONTAR LOS NUMS PARES E IMPARES DEL ARBOL
#primero inserto un nodo en el arbol
def insertar_nodo(raiz, nodo, pos):
    if(raiz is None):
        raiz = NodoArbol(dato, pos)
    elif(dato < raiz.data):
        raiz.izq = insertar_nodo(raiz.izq, dato, pos)
    else:
        raiz.der = insertar_nodo(raiz.der, dato, pos)

#comienza el conteo
cuenta_pares = 0
cuenta_impares = 0
for i in range(rango-1):
    num_aleatorio = random.randint(0, rango)
    if(par(num_aleatorio)):
        cuenta_impares += 1
    else:
        cuenta_pares += 1
    arbol = insertar_nodo(arbol, num_aleatorio)    




