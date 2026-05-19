import networkx as nx
import random

def crear_grafo_aleatorio():

    personas = [
        "Ana", "Luis", "Carlos","Maria", "Pedro", "Juan","Lucia", "Marta"]

    G = nx.Graph()

    G.add_nodes_from(personas)

    for i in range(len(personas)):
        for j in range(i + 1, len(personas)):

            if random.random() < 0.6:

                peso = random.randint(1,5)

                G.add_edge(
                    personas[i],
                    personas[j],
                    weight=peso)

    return G