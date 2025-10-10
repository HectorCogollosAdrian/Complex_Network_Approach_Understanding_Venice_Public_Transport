# Complex Network Approach: Understanding Venice Public Transport

**Mapping Urban Mobility Patterns in Venice Using Complex Network Analysis**

---

## Overview

This project applies **complex network theory** to analyze **Venice’s public transport system**.
By modeling stops and travels as nodes and edges, it explores how **residents and tourists** move through the city.

The goal is to uncover structural patterns, key hubs, and mobility differences between user groups — offering insights for **urban planning** and **transport optimization**.

This repository includes the code and experiments described in the paper "Mapping Urban Mobility Patterns: A Complex Network Approach to Understanding Venice’s Public Transport Usage by Residents and Tourists" submitted to the [IEEE Transactions on Intelligent Transportation Systems](https://ieee-itss.org/pub/t-its/).

---

## Project Structure

```
├── bin/               # Utility scripts for data processing and analysis
├── notebooks/         # Jupyter notebooks with main experiments and visualizations
├── data/              # Input datasets and metadata for network construction
├── models/            # Saved network models (GraphML files and related outputs)
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Requirements

* Python 3.8+
* Libraries:

* geopandas==1.1.1
* libpysal==4.13.0
* matplotlib==3.10.6
* networkx==3.5
* numpy==2.3.3
* pandas==2.3.3

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Clone the repository:

   ```bash
   git clone https://github.com/HectorCogollosAdrian/Complex_Network_Approach_Understanding_Venice_Public_Transport.git
   cd Complex_Network_Approach_Understanding_Venice_Public_Transport
   ```



---

## Methodology

1. Load and clean transport data
2. Build a weighted network (stops = nodes, connections = edges)
3. Compute topological metrics (degree, centrality, modularity, clustering, etc.)
4. Compare **tourist vs resident** mobility networks
5. Visualize key results (maps, graphs, distributions)

---

## Example Results

* Degree and centrality distributions
* Flow maps showing main mobility corridors
* Identification of key transport hubs
* Comparison between tourist and resident network structures

---

## License

Released under the **MIT License**.

---

## Authors

[**Héctor Cogollos Adrián**](https://investigacion.ubu.es/investigadores/131537/detalle?lang=en)  
[**Bruno Baruque Zanón**](https://investigacion.ubu.es/investigadores/35000/detalle)  
[**Santiago Porras Alfonso**](https://investigacion.ubu.es/investigadores/35444/detalle)  
[**Alessandra Raffaetàa**](https://www.unive.it/data/people/5591966)

