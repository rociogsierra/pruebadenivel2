
#Desarrollar un algoritmo que permita cargar 1000 número enteros generados de manera aleatoria

class Node:
    def __int__(self, data):
        self.left = None
        self.right = None
        self.data = data

import random

for i in range(1000):
    print(random.randint(0, 1000))

    

