grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print(grafo["A"])

#------------------------------------------

class Grafo:
  adj = {}

  def _init_(self):
    self.adj = {}

  def adicionar_aresta(self, u, v):
    if u not in self.adj:
      self.adj[u] = []

    if v not in self.adj:
      self.adj[v] = []

    self.adj[u].append(v)
    self.adj[v].append(u)

g1 = Grafo()
g1.adicionar_aresta('A', 'B')
g1.adicionar_aresta('A', 'C')
print(g1.adj)

#------------------------------------------

import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
print(list(G.neighbors('A')))

#------------------------------------------

import matplotlib.pyplot as plt

pos = {
    "A": (0, 1),
    "B": (1, 1),
    "C": (0, 0),
    "D": (1, 0),
    "E": (2, 0)
}

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=900, font_size=14, font_weight="bold")

plt.title("Meu primeiro grafo com NetworkX!")
plt.show()

#------------------------------------------

adjacencia_2 = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

grafo_2 = nx.Graph(adjacencia_2)

pos = nx.spring_layout(grafo_2, seed=42)

nx.draw(grafo_2, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=16, font_weight='bold')

plt.show()

#------------------------------------------

arestas = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'E'), ('C', 'E')]

Grafo_3 = nx.Graph(arestas)

cores_arestas = ["black", "#880000", "black", "black", "black", "red", "#ff0000"]
cores_nodes = ["red", "green", "skyblue", "skyblue", "skyblue"]

nx.draw(Grafo_3, with_labels=True, node_color=cores_nodes, node_size=1200, font_size=16, font_weight="bold", edge_color=cores_arestas)

plt.title("Grafo colorido")
plt.show()

#------------------------------------------

import random

N = 6

vertice_inicial = random.choice(list(grafo_2.nodes))

passeio = []

for i in range(N):
  vizinho = random.choice(list(grafo_2.neighbors(vertice_inicial)))
  passeio.append((vertice_inicial, vizinho))
  vertice_inicial = vizinho

print(f'Arestas do grafo {grafo_2.edges()}')
print(f'Passeio: {passeio}')