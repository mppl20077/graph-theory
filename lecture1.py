import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

# Exercise 1:

def draw_graphs_exercise1():

    # create the graphs
    C5 = nx.cycle_graph(5)
    L33 = nx.grid_2d_graph(3, 3)

    # fix the position to resemble a cartesian plane
    pos = {(i, j): (i, j) for i in range(3) for j in range(3)}

    # create the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

    # draw the first graph on the left subplot
    nx.draw_circular(C5, node_color='black', node_size=100, ax=ax1)
    ax1.set_title('$C_5$')

    # draw the second graph on the right subplot
    nx.draw(L33, pos=pos, node_color='black', node_size=100, ax=ax2)
    ax2.set_title('$L_{3,3}$')

    plt.show()

# Exercise 2
#   
#   G with 20 vertices     
#
#   i) min deg = 0 and max deg = 19
#    
#   ii) min number of edges = 0, max number of edges = 20 over 2 = 20!/(2!(20-2)!) = 20 * 19 / 2 = 190
#    
#   iii) If G has 50 edges then the complement of G will have 190 - 50 = 140 edges

def validate_exercise2():

    # Create two graphs with 20 vertices, one without edges and one comlete
    # so we can test the min and max cases
    G_complete = nx.complete_graph(20)
    G_empty = nx.empty_graph(20)

    print(f'The min deg is {G_empty.degree()[0]} and the max degree is {G_complete.degree()[0]}')
    print(f'The min num of edges is {G_empty.number_of_edges()} and the max num of edges is {G_complete.number_of_edges()}')
   
    G = nx.gnm_random_graph(20, 50)
    print(f'If G has {G.number_of_edges()} then the complement of G has {nx.complement(G).number_of_edges()}')

# Exercise 3

def complements_of_graphs_exercise3():

    # Prepare the two graphs
    G = nx.Graph()
    V = list(range(1,7))
    E = [[1,2],[1,5],[1,6],[2,3],[2,4],[5,6]]
    G.add_nodes_from(V)
    G.add_edges_from(E)

    H = nx.complete_graph(6)

    G_node_labels = {node: f'$v_{node}$' for node in G.nodes()}
    H_node_labels = {node: f'$v_{node}$' for node in H.nodes()}

    # create 4 sublots for each graph and its complement
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))
    ax1, ax2, ax3, ax4 = axes.flatten()

    nx.draw_circular(G, with_labels=True, labels=G_node_labels, node_color='plum', node_size=300, ax=ax1)
    ax1.set_title('G')

    nx.draw_circular(nx.complement(G), with_labels=True, labels=G_node_labels, node_color='plum', node_size=300, ax=ax2)
    ax2.set_title('$G^C$')

    nx.draw_circular(H, with_labels=True, labels=H_node_labels, node_color='plum', node_size=300, ax=ax3)
    ax3.set_title('H')

    nx.draw_circular(nx.complement(H), with_labels=True, labels=H_node_labels, node_color='plum', node_size=300, ax=ax4)
    ax4.set_title('$H^C$')

    plt.show()

# Exercise 4

def draw_2_and_3_regular_graphs_exercise4():

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

    nx.draw_circular(nx.random_regular_graph(2, 10), node_color='black', node_size=200, ax=ax1)
    ax1.set_title('2-regular')

    nx.draw_circular(nx.random_regular_graph(3, 10), node_color='black', node_size=200, ax=ax2)
    ax2.set_title('3-regular')

    plt.show()

# Exercise 5

def check_sequences_exercise5():

    sequences = [
        [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],
        [5, 5, 3, 3, 3, 1],
        [6, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [3, 3, 3, 3, 2, 2, 2, 2, 2],
        [4, 4, 2, 2, 2, 2, 2, 2, 2, 2]
    ]

    for seq in sequences:
        # using havel-hakimi
        is_graphical = nx.is_graphical(seq, method='hh')
        print(f'Sequence {seq} is %s graphical' % ('' if is_graphical else 'not'))

if __name__ == '__main__':

    draw_graphs_exercise1()
    validate_exercise2()
    complements_of_graphs_exercise3()
    draw_2_and_3_regular_graphs_exercise4()
    check_sequences_exercise5()
