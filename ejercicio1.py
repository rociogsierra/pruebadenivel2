#Desarrollar un árbol de decisión para resolver esta tarea
#Creación del árbol
class NodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

#Usaré la función insertar_nodo propuesta en el word de árboles y grafos
#Si la respuesta es sí, se debe desplazar hacia el subárbol izquierdo, si es no al subárbol derecho

def insertar_nodo(raiz, dato, pos):
    if(raiz is None):
        raiz = NodoArbol(dato)
    elif(pos == "Sí"):
        raiz.izq = insertar_nodo(raiz.izq, dato, "Sí")
    else:
        raiz.der = insertar_nodo(raiz.der, dato, "No")
    return raiz
    




