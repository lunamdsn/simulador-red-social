import matplotlib.pyplot as plt
import networkx as nx

plt.ion()

def dibujar_grafo(G, informados=None, pos=None):

    if informados is None:
        informados = []

    plt.clf()

    colores = []
    for nodo in G.nodes():

        if informados and nodo == informados[-1]:
            colores.append("yellow")

        elif nodo in informados:
            colores.append("green")

        else:
            colores.append("skyblue")

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=colores,
        node_size=2000,
        edge_color="gray")

    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels)

    plt.title("Propagación del rumor")

    plt.draw()
    plt.pause(1.0) 