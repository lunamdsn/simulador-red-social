# Simulador de Propagación de Información en Redes Sociales

## Introducción
Este proyecto simula cómo se propaga una información (rumor, noticia o mensaje) dentro de una red social representada mediante un grafo. Cada nodo representa una persona y cada conexión representa una relación entre usuarios. El sistema calcula cómo se propaga la información y cuánto tiempo tarda en llegar a cada persona utilizando el algoritmo de Floyd-Warshall.

Además, se incluye una visualización dinámica del proceso de propagación.


## Características
- Representación de una red social mediante grafos
- Generación aleatoria de usuarios y conexiones
- Implementación del algoritmo Floyd-Warshall
- Simulación paso a paso de la propagación
- Cálculo de tiempos de llegada
- Cálculo de caminos mínimos
- Estadísticas finales
- Visualización dinámica mediante colores


## Tecnologías utilizadas
- Python 3
- NetworkX
- Matplotlib


## Estructura del proyecto
```text
simulador-red-social/
│
├── main.py
├── grafo.py
├── propagacion.py
├── visualizacion.py
├── requirements.txt
├── README.md
└── docs/
    └── documentacion.md
```


## Instalación
Clonar el repositorio:
```bash
git clone (https://github.com/lunamdsn/simulador-red-social.git)
```

Entrar en la carpeta:
```bash
cd simulador-red-social
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```


## Ejecución
Ejecutar el programa:
```bash
python3 main.py
``` 
