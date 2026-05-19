import networkx as nx

def simular_pasos(G, origen):
    distancias = dict(nx.floyd_warshall(G, weight="weight"))

    tiempos = distancias[origen]

    # Ordenar por tiempo de llegada
    orden = sorted(tiempos.items(), key=lambda x: x[1])

    pasos = []

    for i in range(len(orden)):
        paso_actual = [nodo for nodo, _ in orden[:i+1]]
        pasos.append(paso_actual)

    return orden, pasos