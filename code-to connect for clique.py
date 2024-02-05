#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import random

def connect_complete_and_random(n_complete, p_complete, n_random, p_random):
    """
    Connects a complete graph and an Erdős-Rényi random graph.

    Parameters:
    - n_complete: Number of nodes in the complete graph.
    - p_complete: Probability of an edge in the complete graph.
    - n_random: Number of nodes in the random graph.
    - p_random: Probability of an edge in the random graph.

    Returns:
    - G: NetworkX graph.
    """
    G = nx.complete_graph(n_complete)

    # Connect the complete graph and the random graph
    for i in range(n_complete, n_complete + n_random):
        for j in range(i + 1, n_complete + n_random):
            if random.randint(0,1) < p_random:
                G.add_edge(i, j)

    return G


n_complete = random.randint(1,10)  # Number of nodes in the complete graph
p_complete = random.uniform(0,1)  # Probability of an edge in the complete graph (since it's complete)
n_random = random.randint(1,4)  # Number of nodes in the random graph
p_random = random.uniform(0,1)  # Probability of an edge in the random graph
print(n_complete)
print(p_complete)
print(n_random)
print(p_random)
graph = connect_complete_and_random(n_complete, p_complete, n_random, p_random)

# Visualize the graph
nx.draw(graph, with_labels=True)
plt.show()


# In[ ]:




