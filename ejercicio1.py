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

def decision():
    habilidades=nodoArbol("Misiones intergalácticas")
    insertar_nodo(habilidades,"Khan","Si")
    #Khan es ideal para misiones intergalácticas
    insertar_nodo(habilidades,"Misión de recuperación","No")
    #Khan no es ideal para misiones de recuperación
    insertar_nodo(habilidades.der,"Ant-Man","Si")
    #Ant Man es ideal para misiones de recuperación
    insertar_nodo(habilidades.der,"Misión de destrucción","No")
    #Ant Man no es ideal para misiones de destrucción
    insertar_nodo(habilidades.der.der,"Hulk","Si")
    #Hulk es ideal para misiones de destrucción
    insertar_nodo(habilidades.der.der,"Misión de defensa y recuperación","No")
    #Hulk no es ideal para misiones de defensa y recuperación
    insertar_nodo(habilidades.der.der.der,"Capitan América","Si")
    #Capitán América es ideal para misiones de defensa y recuperación
    insertar_nodo(habilidades.der.der.der,"Misión de viaje","No")
    #Capitán América no es ideal para misiones de viaje
    insertar_nodo(habilidades.der.der.der.der,"Capitana Marvel","Si")
    #Capitana Marvel es ideal para misiones de viaje
    insertar_nodo(habilidades.der.der.der.der,"Misión de habilidad","No")
    #Capitana Marvel no es ideal para misiones de habilidad
    insertar_nodo(habilidades.der.der.der.der.der,"Khan","Si")
    #Khan es ideal para misiones de habilidad
    insertar_nodo(habilidades.der.der.der.der.der,"Misión de recuperación e infiltración","No")
    #Khan no es ideal para misiones de recuperacion e infiltracion
    insertar_nodo(habilidades.der.der.der.der.der.der,"The Winter Soldier","Si")
    #The Winter Soldier es ideal para misiones de recuperación e infiltración
    insertar_nodo(habilidades.der.der.der.der.der.der,"Misión de defensa y tecnología","No")
    #The Winter Soldier no es ideal para misiones de defensa y tecnología
    insertar_nodo(habilidades.der.der.der.der.der.der.der,"Iron Man","Si")
    #Iron Man es ideal para misiones de defensa y tecnología
    insertar_nodo(habilidades.der.der.der.der.der.der.der,"Misión rápida","No")
    #Iron Man np es ideal para misiones rápidas
    insertar_nodo(habilidades.der.der.der.der.der.der.der.der,"Nick Fury","Si")
    #Nick Fury es ideal para misiones rápidas
    insertar_nodo(habilidades.der.der.der.der.der.der.der.der,"Misión destruir ejercito","No")
    #Nick Fury no es ideal para misiones de destruir ejércitos
    insertar_nodo(habilidades.der.der.der.der.der.der.der.der.der,"Thor","Si")
    #Thor es ideal para misiones de destruir ejércitos
    insertar_nodo(habilidades.der.der.der.der.der.der.der.der.der,"No hay héroe","No")
    #No se dan más héroes

    return habilidades

def VerMision(superheroes):
    print("Lista de misiones:")
    for i in superheroes:
        print("--->",superheroes[i])

def SeleccionarMision(NombreMision,Escuadron):
    if(Escuadron.izq is None):
        return Escuadron.info
    elif(Escuadron.info==NombreMision):
        return SeleccionarMision(NombreMision, Escuadron.izq)
    else:
        return SeleccionarMision(NombreMision, Escuadron.der)

superheroes = { "Khan" : "Misiones intergalacticas",
"Ant-Man":"Misión de recuperacion",
"Hulk": "Misión de destruccion",
"Capitan America" : "Misión de defensa y recuperacion",
"Capitana Marvel" : "Misión de viaje",
"Khan" : "Misión de habilidad",
"The Winter Soldier" : "Misión de recuperacion e infiltracion",
"Iron Man" : "Misión de defensa y tecnologia",
"Nick Fury" : "Misión rapida",
"Thor" : "Misión destruir ejercito"
}   

EscuadronSHIELD = decision()
VerMision(superheroes)
print("LA MISIÓN SERÁ: ")
Mision = input()
print("la misión {} estará asignada al superheroe {}").format(SeleccionarMision(Mision, EscuadronSHIELD), Mision)




