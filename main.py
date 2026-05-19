from grafo import crear_grafo_aleatorio
from propagacion import simular_pasos
from visualizacion import dibujar_grafo
import networkx as nx
import matplotlib.pyplot as plt

G = crear_grafo_aleatorio()

pos = nx.spring_layout(G, seed=42)

print("Usuarios disponibles:")
print(list(G.nodes()))

origen = input("\n¿Quién inicia el rumor?: ")

while origen not in G.nodes():
    origen = input("Usuario no válido. Introduce otro: ")

orden, pasos = simular_pasos(G, origen)

print("\nSimulación de propagación:\n")

for i, paso in enumerate(pasos):
    print(f"Paso {i}: {paso}")

print("\nTiempo de llegada:\n")

for persona, tiempo in orden:
    print(f"{persona}: {tiempo}")

print("\nEstadísticas:")

print(f"Total usuarios: {len(G.nodes())}")

ultimo = orden[-1]

print(f"Último usuario informado: {ultimo[0]}")
print(f"Tiempo total: {ultimo[1]}")

grado = dict(G.degree())

influyente = max(grado, key=grado.get)

print(f"Usuario más conectado: {influyente}")

print("\nCamino más corto:")

if nx.has_path(G, origen, ultimo[0]):
    camino = nx.shortest_path(G, source=origen, target=ultimo[0], weight="weight")
    distancia = nx.shortest_path_length(G, source=origen, target=ultimo[0], weight="weight")

    print(" -> ".join(camino))
    print(f"Coste total del camino: {distancia}")
else:
    print("No hay conexión entre los usuarios (grafo no conectado)")

for paso in pasos:
    dibujar_grafo(G, paso, pos)

plt.ioff()
plt.show()