from turtle import Turtle
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

# Exrcise 1:

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

    print(f'The min deg is {G_empty.degree()[0]} and the max degree is {G_complete.degree()[0]}');
    print(f'The min num of edges is {G_empty.number_of_edges()} and the max num of edges is {G_complete.number_of_edges()}');
   
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

def check_sequences_exercise5(log_level='info'):

    sequences = [
        [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],
        [5, 5, 3, 3, 3, 1],
        [6, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
        [3, 3, 3, 3, 2, 2, 2, 2, 2],
        [4, 4, 2, 2, 2, 2, 2, 2, 2, 2]
    ]

    if log_level == 'info':

        for seq in sequences:
            # using havel-hakimi
            is_graphical = nx.is_graphical(seq, method='hh')
            print(f'Sequence {seq} is %s graphical' % ('' if is_graphical else 'not'))

    elif log_level == 'verbose':
        
        for seq in sequences:
            print('*' * 20)
            print(f'Start checking for {seq}')
            print('*' * 20)

            check_finished = False

            print(f'Start basic graphical tests')
            # _basic_graphical_tests
            # Sort and perform some simple tests on the sequence
            deg_sequence = deepcopy(seq)
            deg_sequence = nx.utils.make_list_of_ints(deg_sequence)
            p = len(deg_sequence)
            num_degs = [0] * p
            dmax, dmin, dsum, n = 0, p, 0, 0
            for d in deg_sequence:

                # Reject if degree is negative or larger than the sequence length
                if d < 0:
                    print(f'The sequence contains node with d = {d} < 0')
                    print('The sequence is not graphical')
                    check_finished = True
                    break
                elif d >= p:
                    print(f'The sequence contains node with d = {d} > {p} which is the length of the sequence')
                    print('The sequence is not graphical')
                    check_finished = True
                    break
                # Process only the non-zero integers
                elif d > 0:
                    dmax, dmin, dsum, n = max(dmax, d), min(dmin, d), dsum + d, n + 1
                    num_degs[d] += 1
            
            if check_finished:
                continue

            print('The sequence has values:')
            print(f'dmax = {dmax}, dmin = {dmin}, dsum = {dsum}, n = {n}, num_degs = {num_degs}')
            # Reject sequence if it has odd sum or is oversaturated
            if dsum % 2:
                print(f'The sequence has odd dsum = {dsum}')
                print('The sequence is not graphical')
                continue
            elif dsum > n * (n - 1):
                print(f'The sequence is oversaturated dsum = {dsum} > n * (n - 1)')
                print('The sequence is not graphical')
                continue
            
            if n == 0:
                print(f'The sequence has no non-zero degrees n = {n}')
                print('The sequence is graphical')
                continue

            print('Start Havel-Hakimi test')
            print('Test first the ZZ condition:') 
            print('If 4 * dmin * n >= (dmax + dmin + 1) * (dmax + dmin + 1) then the sequence is graphical')
            if 4 * dmin * n >= (dmax + dmin + 1) * (dmax + dmin + 1):
                print('The sequence passes the ZZ condition')
                print('The sequence is graphical')
                continue
            
            #  Havel-Hakimi
            modstubs = [0] * (dmax + 1)
            # Successively reduce degree sequence by removing the maximum degree
            while n >= 0:
                print(f'Remaining number of non-zero degree vertices n = {n}')
                print(f'Remaining num_degs = {num_degs}')

                if n == 0:
                    print('The sequence is graphical')
                    break;

                # Retrieve the maximum degree in the sequence
                print(f'The max degree is dmax = {dmax}')
                while num_degs[dmax] == 0:
                    print(f'There is not a vertex with d = dmax = {dmax}')
                    dmax -= 1
                    print(f'continue with dmax = {dmax}')
                # If there are not enough stubs to connect to, then the sequence is
                # not graphical
                if dmax > n - 1:
                    print(f'The number of non-zero degree vertices is n = {n} and dmax = {dmax}')
                    print('So, there are not enough vertices to connect the vertex with the max degree')
                    print('The sequence is not graphical')
                    break

                # Remove largest stub in list
                print('Remove vertices with the largest degree and reaarrange the rest edges in lower degrees')
                num_degs[dmax], n = num_degs[dmax] - 1, n - 1
                # Reduce the next dmax largest stubs
                mslen = 0
                k = dmax
                for i in range(dmax):
                    while num_degs[k] == 0:
                        k -= 1
                    num_degs[k], n = num_degs[k] - 1, n - 1
                    if k > 1:
                        modstubs[mslen] = k - 1
                        mslen += 1
                # Add back to the list any non-zero stubs that were removed
                for i in range(mslen):
                    stub = modstubs[i]
                    num_degs[stub], n = num_degs[stub] + 1, n + 1
                    
            
    else:
        print("The supported log levels are 'info' and 'verbose'")


if __name__ == '__main__':

    draw_graphs_exercise1()
    validate_exercise2()
    complements_of_graphs_exercise3()
    draw_2_and_3_regular_graphs_exercise4()
    check_sequences_exercise5(log_level='verbose')
