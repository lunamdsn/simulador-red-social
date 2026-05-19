import matplotlib.pyplot as plt
import networkx as nx

ax = None

def iniciar_grafico():
    global ax
    plt.ion()
    fig, ax = plt.subplots()

def dibujar_grafo(G, informados=None, pos=None):

    global ax 

    if ax is None:
        iniciar_grafico()

    if informados is None:
        informados = []

    ax.clear()

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
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    ax.set_title("Propagación del rumor")

    plt.draw()