# connecting-complete-graph-and-random-graph-
This is a code to connect a complete graph(clique) and a random Erdos-Rnyi graph.
 Parameters:
    - n_complete: Number of nodes in the complete graph.
    - p_complete: Probability of an edge in the complete graph.
    - n_random: Number of nodes in the random graph.
    - p_random: Probability of an edge in the random graph.
Psuedo Code
 1. First generate a random complete graph G 
 2. For every n_complete and the total no.of nodes(n_complete+n_random)
    2.1and for every adjacent node to the current node(i+1) ,check if a random number is less than the p_random.
    2.2 if yes then add and edge, else do not add an edge
3. Return the graph.
