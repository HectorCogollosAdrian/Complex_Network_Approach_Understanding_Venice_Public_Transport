import networkx as nx
import pandas as pd
import pickle


def __community__(nodo, community):
    """
    Look for the community that a node belongs to.
    :param nodo: The node for which you want to know the community.
    :type nodo: String
    :param community:
    :type community: List of List
    :return: The community to which the node belongs.
    :rtype: int
    """
    for c, i in enumerate(community):
        if nodo in i:
            return c


def __comu_degree__(x, sub_graph, weight = None):
    """
    Returns the degree of a node within a community.
    :param x: Node
    :type x: String
    :param sub_graph: A subgraph formed by a single community.
    :type sub_graph: SubGraph View
    :param weight: Weight attribute of the graph
    :type weight: String
    :return: node degree in the community
    :rtype: float
    """
    a = sub_graph.degree(weight = weight, nbunch = x)
    if isinstance(a, float):
        return a
    else:
        return None

def to_picle(dZ,dP,dRol,cm,n_file):
    """
    Save the results of the guimera algorithm and the communities in pickle files
    :param dZ: Dictionary of Z score
    :type dZ: dict
    :param dP: Dictionary of P value
    :type dP: dict
    :param dRol: Dictionary of roles
    :type dRol: dict
    :param cm: Node communities
    :type cm: List of List
    :param n_file: file names
    :type n_file: String

    """
    with open(n_file+'_z.pickle', 'wb') as pickled_file:
        pickle.dump(dZ,pickled_file)
    with open(n_file+'_p.pickle', 'wb') as pickled_file:
        pickle.dump(dP,pickled_file)
    with open(n_file + '_rol.pickle', 'wb') as pickled_file:
        pickle.dump(dRol, pickled_file)
    with open(n_file+'_comunity.pickle', 'wb') as pickled_file:
        pickle.dump(cm,pickled_file)


def rol(dZ, dP):
    """
    Calculate the role to which each node belongs using its z-score and P-value.
    :param dZ: Dictionary of Z-score
    :type dZ: dict
    :param dP: Dictionary of P-value
    :type dP: dict
    :return: Dictionary with node roles
    :rtype: dict
    """
    dRol = dict()
    for i in dZ:
        if dZ[i]>=2.5:
            if dP[i]<0.31:
                dRol[i]="R5 Provincial hubs"
            elif dP[i]<0.75:
                dRol[i] = "R6 Connector hubs"
            else:
                dRol[i] = "R7 Kinless hubs"
        else:
            if dP[i]<0.05:
                dRol[i]="R1 Ultra-peripheral"
            elif dP[i]<0.625:
                dRol[i]="R2 Peripheral"
            elif dP[i]<0.8:
                dRol[i]="R3 Non-hub connectors"
            else:
                dRol[i] = "R4 Non-hub kinless"
    return dRol


def guimera(G, cm, weight=None):
    """
    Guimera algorithm that calculates the role of nodes in their community using z-score and P-value
    :param G: Graph
    :type G: DiGraph
    :param cm: Node communities
    :type cm: List of List
    :param weight: Weight attribute of the graph
    :type weight: String
    :return: z-score and P-value
    :rtype: dict, dict
    """
    dgMean = dict()
    dgSTD = dict()
    dZ = dict()
    dP = dict()

    #Sub Graph
    subGraphs = dict()
    for c,i in enumerate(cm):
        subGraphs[c] = G.subgraph(i)
    #node Table
    dfNodes = pd.DataFrame({'node':G.nodes})
    #Add Community
    dfNodes['community'] = dfNodes['node'].map(lambda x: __community__(x, cm))
    #TOTAL deggre of nodes
    dfNodes['degree_t'] = dfNodes['node'].map(lambda x: G.degree(weight=weight, nbunch=x))
    #Deggre of the community
    for i in range(len(cm)):
        dfNodes['degree_community_' + str(i)] = dfNodes['node'].map(lambda x: __comu_degree__(x,subGraphs[i],weight=weight))
    for i in range(len(cm)):
        dgMean['degree_community_'+str(i)] = dfNodes['degree_community_' + str(i)].mean()
        dgSTD['degree_community_'+str(i)] = dfNodes['degree_community_' + str(i)].std()
    #Grade of the remaining communities...(the n communities)

    for i in dfNodes['node'].to_list():
        comu = dfNodes[dfNodes['node'] == i].community.to_list()[0]
        std = dgSTD['degree_community_'+str(comu)]
        if std == 0:
            dZ[i] = 0
        else:
            dZ[i] = (dfNodes[dfNodes['node']==i].degree_t.to_list()[0]-dgMean['degree_community_'+str(comu)])/std

    for j in dfNodes['node'].to_list():
        dP[j]=1
        aux = 0
        for i in cm:
            c = i.copy()
            c.add(j)
            aux = aux+((G.subgraph(c).degree(weight=weight, nbunch=j)/dfNodes[dfNodes['node']==j].degree_t.to_list()[0])**2)
        dP[j] = dP[j]-aux
    return dZ,dP


