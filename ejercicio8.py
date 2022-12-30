
#Desarrollar un algoritmo que permita cargar 1000 número enteros generados de manera aleatoria

class Nodo:
    def __int__(self, data):
        self.izq = None
        self.der = None
        self.data = data

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
