# -*- coding: utf-8 -*-
import heapq
import math

def flood_it(matrix):
    # Define a função heurística: distância euclidiana
    def heuristic(a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    # Define a função de expansão de nó: retorna os vizinhos do nó atual
    def expand(node):
        x, y = node
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if x < len(matrix)-1:
            neighbors.append((x+1, y))
        if y < len(matrix[0])-1:
            neighbors.append((x, y+1))
        return neighbors
    
    # Define a função de custo de movimento: retorna o custo de se mover de um nó para outro
    def move_cost(a, b):
        x1, y1 = a
        x2, y2 = b
        return abs(matrix[x1][y1] - matrix[x2][y2])
    
    # Inicializa o estado inicial e a lista de nós a serem explorados
    start = (0,0)
    goal = (len(matrix)-1, len(matrix[0])-1)
    frontier = []
    heapq.heappush(frontier, (0, start))
    explored = set()
    parent = {start: None}
    cost_so_far = {start: 0}
    
    # Loop principal do algoritmo A*
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            # Chegamos ao objetivo, retorna o caminho até o estado inicial
            path = [current]
            while current != start:
                current = parent[current]
                path.append(current)
            path.reverse()
            return path
        
        explored.add(current)
        
        for neighbor in expand(current):
            new_cost = cost_so_far[current] + move_cost(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                parent[neighbor] = current
    
    # Não foi possível encontrar um caminho até o objetivo
    return None

# Lê o arquivo de entrada
with open('matrix.txt', 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]

# Resolve o jogo Flood-It e imprime a solução
path = flood_it(matrix)
if path is not None:
    print('Tamanho da solução: {}'.format(len(path)))
   # print(f'Tamanho da solução: {len(path)}')
    print('Caminho até o objetivo:')
    for node in path:
        print(node)
else:
    print('Não foi possível encontrar uma solução.')
