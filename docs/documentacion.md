# Documentación técnica del proyecto Simulador de Propagación de Información en Redes Sociales


# 1. Descripción
El objetivo de este proyecto es desarrollar un simulador de propagación de información en una red social utilizando estructuras de grafos y algoritmos de caminos mínimos. El programa representará una red social donde cada nodo corresponde a una persona y cada arista representa una conexión entre usuarios. Además, cada conexión tendrá un peso asociado que simboliza el tiempo o dificultad de transmisión de la información entre dos personas.

El código se organizará en distintos módulos para facilitar su mantenimiento y comprensión. El archivo main.py actuará como punto de entrada principal y coordinará la ejecución del programa. grafo.py se encargará de generar automáticamente la red social mediante un grafo aleatorio. propagacion.py contendrá la lógica de simulación utilizando el algoritmo de Floyd-Warshall para calcular las distancias mínimas entre nodos, mientras que visualizacion.py gestionará la representación gráfica del proceso mediante animaciones y cambios de color.

El programa permitirá seleccionar el usuario inicial que comenzará la propagación de la información. Después se calculará el tiempo de llegada a cada usuario, el orden de propagación y el camino mas corto utilizado. Además, se mostrarán estadísticas adicionales como el tiempo total de difusión y el usuario con mayor número de conexiones.

Para desarrollar el proyecto se utilizarán las bibliotecas NetworkX para la creación y manipulación de grafos y Matplotlib para las visualizaciones gráficas. 

# 2.Algoritmo 

Se utiliza el algoritmo de Floyd-Warshall para calcular los caminos más cortos entre todos los pares de nodos del grafo.

El algoritmo evalúa si un nodo intermedio puede mejorar la distancia entre dos nodos. Si se encuentra un camino más corto, se actualiza la matriz de distancias.



# 3. Complejidad

La complejidad temporal es: O(n³)

Esto se debe a que se evalúan todas las combinaciones posibles de nodos como intermediarios.



# 4. Aplicación en este proyecto

- Nodo: persona
- Arista: conexión social
- Peso: tiempo de transmisión

El algoritmo permite calcular: Quién recibe el mensaje primero. Cuánto tarda en llegar a cada usuario. La ruta más eficiente de propagación

Una vez calculadas las distancias mínimas, se simula la propagación del rumor desde un nodo inicial. La información se propaga progresivamente según los tiempos calculados, mostrando el orden de llegada de cada usuario.

La versión final incorpora generación aleatoria de redes sociales, permitiendo que cada ejecución produzca estructuras distintas y resultados diferentes en la propagación de la información.



# 5. Visualización

Se utiliza la librería Matplotlib junto con NetworkX para representar el grafo.

Durante la simulación los nodos cambian de color cuando reciben la información, se muestra la evolución paso a paso, se representan los pesos de las conexiones.

El usuario puede seleccionar el nodo inicial desde el que comienza la difusión.



# 6. Conclusión

Este modelo permite analizar cómo la estructura de una red social influye directamente en la velocidad de propagación de la información. Redes más conectadas o con menores pesos permiten una difusión más rápida del mensaje.



# 7. Mejoras implementadas

- Generación aleatoria de redes sociales.
- Selección interactiva del usuario inicial.
- Cálculo del usuario más conectado.
- Estadísticas finales de propagación.
- Visualización dinámica con distintos colores.
- Cálculo y visualización de caminos mínimos.