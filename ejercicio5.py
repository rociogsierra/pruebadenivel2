
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

#Algoritmo de Prim = Árbol de expansión máxima
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
	printMaximumSpanningTree(graph, parent);


#Número de vertices
V = 8;

#Punto A:
print('Punto A:')

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

grafo = [
    [0, 6, 0, 1, 8, 7, 3, 2],
    [6, 0, 0, 6, 1, 8, 9, 1],
    [0, 0, 0, 1, 2, 1, 5, 0],
    [1, 6, 1, 0, 1, 5, 9, 3],
    [8, 1, 2, 1, 0, 2, 4, 5],
    [7, 8, 1, 5, 2, 0, 1, 6],
    [3, 9, 5, 9, 4, 1, 0, 1],
    [2, 1, 0, 3, 5, 6, 1, 0]];

print('Diccionario con los nombres de superhéroes y vértices del grafo:', nombres_superheroes)
print('Grafo', grafo)

print('\nPunto b:')
print('Árbol de expansión máximo:')
print(maximumSpanningTree(grafo));
print('\nPunto c:')

#Determinar el máximo de episodios entre superhéroes
maxEpisodios = max([max(vertices) for vertices in grafo])
print('El número máximo de episodios entre superhéroes es {}'.format(maxEpisodios))

#Determinar qué superhéoes tienen 9 episodios en común
for ind, vertices in enumerate(grafo):
    for ind2, peso in enumerate(vertices[:ind]):
        if peso == maxEpisodios:
            print('{} y {} tienen {} episodios en común.'.format(nombres_superheroes[ind], nombres_superheroes[ind2], maxEpisodios))
        
print('\nPuntos D y E:')

#Determinar el número de episodios de cada superhéroe en la saga
for ind, vertices in enumerate(grafo):
    if sum(vertices) == 9:
        print('{} aparece en exactamente {} episodios de la saga'.format(nombres_superheroes[ind], 9))