
#pila de cartas de las cuales se conoce su número y palo (mazo de cartas de baraja española)


#primero generaro una baraja

valores = ["as", "2", "3", "4", "5", "6", "7", "sota", "caballo", "rey"]
palos = ["oros", "copas", "espadas", "bastos"]
mazo = []

for valores in valor:
    for palo in palos:
        carta = "{} de {}".format(valores, palos)
        baraja.append(carta)
print(baraja)



