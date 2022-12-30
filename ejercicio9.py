
#pila de cartas de las cuales se conoce su número y palo (mazo de cartas de baraja española)


#primero genero un mazo

valores = ["as", "2", "3", "4", "5", "6", "7", "sota", "caballo", "rey"]
palos = ["oros", "copas", "espadas", "bastos"]
mazo = []

#genero un bucle para ver todo el mazo

for valores in valor:
    for palo in palos:
        carta = "{} de {}".format(valores, palos)
        mazo.append(carta)
print(mazo)

#generar las cartas del mazo de forma aleatoria

import random

unir = f" {valores} {palos}"
longitud = 40

extension = random.sample(unir, longitud)
mazo_aleatorio = "".join(extension)

print(mazo_aleatorio)

#ordenar el mazo

for m in range(0, 40, 4):
    print("{} {} {} {}".format(mazo[m], mazo[m+1], mazo[m+2], mazo[m+3]))

#esta es una forma de resolver el ejercicio, aunque entiendo que hay que hacerlo con pilas:

#genero la baraja

class carta:  
    lista_de_palos = ["oros", "copas", "espadas", "bastos"]
    lista_de_valores = ["as", "2", "3", "4", "5", "6", "7", "sota", "caballo", "rey"]

    def __init__(self, palo=0, valor=0):
        self.palo = palo
        self.valor = valor

    def __str___(self):
        return(self.lista_de_valores[self.valor] + "de" + self.lista_de_palos[self.palos])

class baraja:
    def __init__(self):
        self.todas_las_cartas = []
        for palo in range(4):
            for valor in range(1, 40):
                self.cartas.append(carta(palo, valor))

def mostrar_la_baraja(self):
    for carta in self.todas_las_cartas:
        print(carta)

def __str__(self):
    s = ""
    for i in range(len(self.todas_las_cartas)):
        s = s + " "*i + str(self.cartas[i]) + "n"
        return s

#generar las cartas de la baraja de forma aleatoria

def mezclar_las_cartas(self):
    nuevas_cartas = len(self.todas_las_cartas)
    for i in range(nuevas_cartas):
        j = random.randrange(i, nuevas_cartas)
        self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

#separar la pila baraja en cuatro pilas una por cada palo

class oros():
    def __init__(self, num):
        self.num = num

    def __str___(self):
        return "{} de oros".format(self.num)


class copas():
    def __init__(self, num_2):
        self.num_2 = num_2

    def __str___(self):
        return "{} de copas".format(self.num_2)


class espadas():
    def __init__(self, num_3):
        self.num_3 = num_3

    def __str___(self):
        return "{} de espadas".format(self.num_3)


class bastos():
    def __init__(self, num_4):
        self.num_4 = num_4

    def __str___(self):
        return "{} de bastos".format(self.num_4)


#ordenar una de las cuatro pilas(oros, copas, espadas, bastos) de manera creciente
def Orden(cartas):
    for i in range(len(cartas)):
        mini = i
        for j in range(i+1, len(cartas)):
            if cartas[j] < cartas[mini]:
                mini = j
    cartas[i], cartas[mini] = cartas[mini], cartas[i]
    return cartas


Baraja_en_orden = []
for i in lista_de_palos:
    for j in lista_de_valores:
        Baraja_en_orden.append([i, j])

