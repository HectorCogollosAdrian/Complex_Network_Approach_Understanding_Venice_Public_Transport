import random
import networkx as nx

### Implementation of the Rewiring algorithm

# The rewiring algorithm creates a random version of the original network by keeping the same set of nodes and redistributing the existing edge weights among randomly selected node pairs. 
# This preserves the number of edges and the weight distribution, but randomizes the connections, allowing comparison of structural properties with the original network

def rewiring(G_original): 
    """
    Using the original network, redistribute the links and weights
    :param G_original: networkX DiGraph 
    :type G_original: Graph
    :return: new rewiring graph with weights
    :rtype: DiGraph
    """
    #Obtain original nodes and weights
    nodos = list(G_original.nodes())
    pesos = [G_original[u][v]['weight'] for u, v in G_original.edges()]
    num_aristas = G_original.number_of_edges()
    
    #Create new network with same nodes
    G_random = nx.DiGraph()  # o nx.Graph() si no dirigida
    G_random.add_nodes_from(nodos)
    
    #Generate random edges without repetition 
    posibles_aristas = [(u, v) for u in nodos for v in nodos if u != v]
    aristas_aleatorias = random.sample(posibles_aristas, num_aristas)
    
    #Mix the weights 
    random.shuffle(pesos)
    
    #Assign weights to random edges
    for (u, v), peso in zip(aristas_aleatorias, pesos):
        G_random.add_edge(u, v, weight=peso)
    return G_random


### Implementation of the Erdos Renyi algorihtm

# The Erdős-Rényi model generates random graphs by connecting pairs of nodes with edges chosen uniformly at random. In its simplest form, each possible edge between nodes is included with a fixed probability, or a fixed number of edges is distributed randomly among all possible node pairs. 
# This produces networks with no inherent structure, serving as a baseline for comparison with real-world networks.

def erdos_renyi_weighted_same_nodes(G_original, weight_range=(0.1, 1.0), directed=True, seed=None):
    """
    Generates an Erdős-Rényi network with the same nodes and number of edges as G_original, and assigns random weights to the edges.
    :param G_original: networkX DiGraph.
    :type G_original: DiGraph
    :param weight_range: tuple with the range of weights (min, max)
    :type weight_range: tuple
    :param directed: if True, generates a directed graph
    :type directed: bool
    :param seed: optional random seed
    :type seed: int
    :return: new random graph with weights
    :rtype: DiGraph
    """
    
    rng = random.Random(seed)
    n = G_original.number_of_nodes()
    m = G_original.number_of_edges()
    
    # Create an empty graph with the same nodes
    G_rand = nx.DiGraph() if directed else nx.Graph()
    G_rand.add_nodes_from(G_original.nodes())

    possible_edges = [(u, v) for u in G_rand.nodes() for v in G_rand.nodes() if u != v]
    if not directed:
        possible_edges = [(u, v) for u, v in possible_edges if u < v]

    rng.shuffle(possible_edges)
    selected_edges = possible_edges[:m]

    for u, v in selected_edges:
        weight = rng.uniform(*weight_range)
        G_rand.add_edge(u, v, weight=weight)

    return G_rand