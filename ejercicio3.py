import sys

def findMaxVertex(visited, weights):
	index = -1;
	maxW = -sys.maxsize;
	for i in range(V):
		if (visited[i] == False and weights[i] > maxW):
			maxW = weights[i];
			index = i;
	return index;

def printMaximumSpanningTree(graph, parent):
	MST = 0;
	for i in range(1, V):
		MST += graph[i][parent[i]];
	print("Peso del árbol máximo de expansión: ", MST);
	print();
	print("Arista \tPeso");
	for i in range(1, V):
		print(parent[i] , " - " , i , " \t" , graph[i][parent[i]]);


def maximumSpanningTree(graph):
	visited = [True]*V;
	weights = [0]*V;
	parent = [0]*V;

	for i in range(V):
		visited[i] = False;
		weights[i] = -sys.maxsize; 
	weights[0] = sys.maxsize;
	parent[0] = -1;

	for i in range(V - 1):
		maxVertexIndex = findMaxVertex(visited, weights);
		visited[maxVertexIndex] = True;
		for j in range(V):
			if (graph[j][maxVertexIndex] != 0 and visited[j] == False):
				if (graph[j][maxVertexIndex] > weights[j]):
				
					weights[j] = graph[j][maxVertexIndex];
					parent[j] = maxVertexIndex;

	#Mostrar el árbol de máxima expansión
	printMaximumSpanningTree(graph, parent);

#Número de vertices
V = 8;

#Puntos A y B
print('Puntos A y B:')

graph_twitter = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]];
print('Grafo twitter:', graph_twitter)

graph_instagram = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]];
print('\nGrafo Instagram:', graph_instagram)

nombres_superheroes = {
        0:'Iron Man',
        1:'Hulk',
        2:'Khan',
        3:'Thor',
        4:'Captain America',
        5:'Ant-Man',
        6:'Nick Fury - S.H.I.E.L.D.',
        7:'The Winter Soldier'
    }

#Punto C: Algoritmo Prim para el arbol de expansión máximo
print('\nPunto c:')
print('Twitter')
print(maximumSpanningTree(graph_twitter));

print('\nInstagram')
print(maximumSpanningTree(graph_instagram));	

#Punto D: 
print('\nPunto d:')
print('Capitana Marvel no se encuentra representada en el grafo')

#Punto E:
print('\nPunto e')
#The winter soldier es el último superheroe
#Iron man es el primer superheroe
if graph_twitter[-1][0]!= 0 and graph_twitter[0][-1]!=0:
	print('Es posible conectar a Iron man con The Winter Soldier por Twitter, ya que son amigos')
 
if graph_instagram[-1][0]!= 0 and graph_instagram[0][-1]!=0:
	print('Es posible conectar a Iron man con The Winter Soldier por Instagram, ya que son amigos')

#Punto F:
print('\nPunto f')
for ind, vecino in enumerate(graph_instagram[3]):
	if vecino != 0:
		print('Thor sigue a {}'.format(nombres_superheroes[ind]))