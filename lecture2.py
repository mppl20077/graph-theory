import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from networkx.algorithms.cuts import normalized_cut_size
from networkx.algorithms.community import kernighan_lin_bisection

# Exercise 1

def paths_exercise1():

    # Prepare the graph
    G = nx.Graph()
    G.add_node(1, pos=(0.5, 3*0.866))
    G.add_node(2, pos=(1, 2*0.866))
    G.add_node(3, pos=(2, 2*0.866))
    G.add_node(4, pos=(2.5, 0.866))
    G.add_node(5, pos=(3, 2*0.866))
    G.add_node(6, pos=(3.5, 0.866))
    G.add_node(7, pos=(0, 2*0.866))
    G.add_node(8, pos=(1.5, 0.866))
    G.add_node(9, pos=(2, 0))
    E = [[1,2],[1,7],[2,3],[2,7],[2,8],[3,8],[3,4],[4,8],[4,9],[4,5],[5,6],[8,9]]
    G.add_edges_from(E)
    G_node_labels = {node: f'$v_{node}$' for node in G.nodes()}
    G_node_positions = nx.get_node_attributes(G,'pos')

    fig, axes = plt.subplots(nrows=3,ncols=4, figsize=(80, 60))
    ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12 = axes.flatten()
    options = {
        'pos': G_node_positions,
        'with_labels': True, 
        'labels': G_node_labels, 
        'node_color':'plum', 
        'node_size':300
    }
    nx.draw(G, ax=ax1, **options)
    ax1.set_title('G')

    # i) walk of length 8 from v1 to v3
    edges_i = [
        (1, 2), 
        (1, 7),
        (2, 7),
        (2, 8),
        (8, 9),
        (4, 9),
        (3, 4)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_i} 
    edge_widths = {edge: 4 for edge in edges_i}

    nx.draw(G, ax=ax2, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax2.set_title('$i)\:(v_1,v_2,v_7,v_1,v_2,v_8,v_9,v_4,v_3)$')

    # ii) trail of length 5 from v3 to v8
    edges_ii = [
        (2, 3), 
        (2, 8),
        (8, 9),
        (4, 9),
        (4, 8)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_ii} 
    edge_widths = {edge: 4 for edge in edges_ii}

    nx.draw(G, ax=ax3, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax3.set_title('$ii)\:(v_3,v_2,v_8,v_9,v_4,v_8)$')

    # iii) path of length 4 from v2 to v3
    edges_iii = [
        (2, 8),
        (8, 9),
        (4, 9),
        (3, 4)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_iii} 
    edge_widths = {edge: 4 for edge in edges_iii}

    nx.draw(G, ax=ax4, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax4.set_title('$iii)\:(v_2,v_8,v_9,v_4,v_3)$')

    # iv) closed walk of length 6 (not a trail)
    edges_iv = [
        (1, 2),
        (2, 7),
        (1, 7)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_iv} 
    edge_widths = {edge: 4 for edge in edges_iv}

    nx.draw(G, ax=ax5, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax5.set_title('$iv)\:(v_1,v_2,v_7,v_1,v_2,v_7,v_1)$')

    # v) closed trail of length 6 (not a cycle)
    edges_v = [
        (1, 2),
        (2, 3),
        (3, 8),
        (2, 8),
        (2, 7),
        (1, 7)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_v} 
    edge_widths = {edge: 4 for edge in edges_v}

    nx.draw(G, ax=ax6, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax6.set_title('$v)\:(v_1,v_2,v_3,v_8,v_2,v_7,v_1)$')

    # vi) cycle of length 5
    edges_vi = [
        (2, 3),
        (3, 4),
        (4, 9),
        (8, 9),
        (2, 8)
    ]
    edge_colors = {edge: 'deeppink' for edge in edges_vi} 
    edge_widths = {edge: 4 for edge in edges_vi}

    nx.draw(G, ax=ax7, 
            edge_color=[edge_colors.get(edge, 'black') for edge in G.edges()],
            width=[edge_widths.get(edge, 1) for edge in G.edges()],
            **options)
    ax7.set_title('$vi)\:(v_2,v_3,v_4,v_9,v_8,v_2,v_3)$')

    # vii) acyclic subgraph H that V(H) = V(G)

    # Get all possible combinations of edges to remove
    edges_to_remove = []
    for i in range(1, len(G.edges())):
        edges_to_remove.extend(list(combinations(G.edges(), i)))

    # Check each combination of edges if it results in an acyclic graph
    # and also take the connected ones just for the beauty of it
    acyclic_graphs = []
    for edges in edges_to_remove:
        G_copy = G.copy()
        G_copy.remove_edges_from(edges)
        if nx.is_connected(G_copy) and nx.is_forest(G_copy):
            acyclic_graphs.append(G_copy)
    
    # Just print the first of the list as the example
    nx.draw(acyclic_graphs[0], ax=ax8, **options)
    ax8.set_title('H')

    # viii) Find every cut point and every bridge
    nx.draw(G, ax=ax9, **options)
    for edge in nx.bridges(G):
        nx.draw_networkx_edges(G.subgraph(edge), G_node_positions, edge_color='crimson',width=4, ax=ax9)
    for vertex in nx.articulation_points(G):
        nx.draw_networkx_nodes(G.subgraph(vertex),G_node_positions,node_color='palegreen',node_size=600, ax=ax9)
    ax9.set_title('Bridges and Cut Points')

    # ix) Find the blocks
    nx.draw(G, ax=ax10, **options)
    block_color = ['firebrick', 'gold', 'palegreen', 'royalblue'] 
    for i, block in enumerate(nx.biconnected_components(G)):
        nx.draw_networkx_edges(G.subgraph(block), G_node_positions, edge_color=block_color[i],width=4, ax=ax10)
    ax10.set_title('Blocks')

    ax11.set_axis_off()
    ax12.set_axis_off()

    plt.show()

# Exercise 2

def check_if_biconnected_find_cut_points_exercise2():

    G = nx.Graph()
    G.add_node(1, pos=(0, 3))
    G.add_node(2, pos=(2, 3))
    G.add_node(3, pos=(4, 3))
    G.add_node(4, pos=(6.5, 3))
    G.add_node(5, pos=(6.5, 0))
    G.add_node(6, pos=(4.5, 0))
    G.add_node(7, pos=(2, 0))
    G.add_node(8, pos=(0, 0))
    G.add_node(9, pos=(0, 1.5))
    G.add_node(10, pos=(5, 1.5))
    E = [[1,2],[1,9],[2,3],[2,6],[2,7],[2,9],[3,4],[3,7],[3,10],
         [4,5],[4,10],[5,6],[5,8],[6,7],[6,10],[7,8],[8,9]]
    G.add_edges_from(E)
    G_node_labels = {node: '$v_{' + str(node) +'}$' for node in G.nodes()}
    G_node_positions = nx.get_node_attributes(G,'pos')

    k = nx.edge_connectivity(G)
    
    options = {
        'pos': G_node_positions,
        'with_labels': True, 
        'labels': G_node_labels, 
        'node_color':'plum',
        'node_size':300
    }

    plt.figure(figsize=(12,6))
    plt.title(f'G | {k}-connected | Cut Points')

    # draw the whole graph without the edge (5,8) which will be drawn
    # as a custom curved line
    edge_list = list(G.edges())
    edge_list.remove((5,8))
    nx.draw(G, edgelist=edge_list, **options)

    # Draw the edge between nodes 5 and 8 with a curved line
    # It should be easier...
    ax = plt.gca()
    ax.annotate("",
                xy=G_node_positions[5], xycoords='data',
                xytext=G_node_positions[8], textcoords='data',
                arrowprops=dict(arrowstyle="-", color="black",
                                shrinkA=9, shrinkB=9,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0.2",
                                ),
                )
    
    # We can find all the k_separators and just print one pair as it is asked in 
    # the excercise instructions 
    k_separators = list(nx.all_node_cuts(G))
    nx.draw_networkx_nodes(G.subgraph(k_separators[0]),G_node_positions,node_color='firebrick',node_size=600)

    plt.show()

# Exercise 3

def find_partition_exercise3():

    G = nx.Graph()
    G.add_node(1, pos=(0,0))
    G.add_node(2, pos=(1,0))
    G.add_node(3, pos=(0,1))
    G.add_node(4, pos=(1,1))
    G.add_node(5, pos=(2,1))
    G.add_node(6, pos=(3,0))
    G.add_node(7, pos=(3,1))
    G.add_node(8, pos=(4,0))
    E = [[1,2],[1,3],[2,3],[2,4],[3,4],[4,5],[5,6],[5,7],[6,7],[7,8]]
    G.add_edges_from(E)
    G_node_labels = {node: '$v_{' + str(node) +'}$' for node in G.nodes()}
    G_node_positions = nx.get_node_attributes(G,'pos')    
    
    # find a partition with a normalized cut below 0.5 and lets keep the best
    best_partition = None
    best_normalized_cut = 1.0
    for i in range(10):
        partition = kernighan_lin_bisection(G)
        normalized_cut = normalized_cut_size(G, partition[0], partition[1])
        if normalized_cut < 0.5 and normalized_cut < best_normalized_cut:
            best_partition = partition
            best_normalized_cut = normalized_cut

    options = {
        'pos': G_node_positions,
        'with_labels': True, 
        'labels': G_node_labels, 
        'node_color':'plum',
        'node_size':300
    }

    plt.figure(figsize=(12,4))

    if best_partition != None:
        plt.title(f'G partition:{best_partition}, ncut={best_normalized_cut:.4f}')
    else:
        plt.title('G')
    plt.axis('equal')
    nx.draw(G, **options)
    
    if best_partition != None:
        nx.draw_networkx_nodes(G.subgraph(best_partition[0]),G_node_positions,node_color='firebrick',node_size=300)
        nx.draw_networkx_nodes(G.subgraph(best_partition[1]),G_node_positions,node_color='gold',node_size=300)

    plt.show()

# Exercise 4

def check_if_euler_exercise4():

    G1 = nx.Graph()
    G1.add_node(1, pos=(0,0))
    G1.add_node(2, pos=(0,1))
    G1.add_node(3, pos=(0.866,0.5))
    G1.add_node(4, pos=(1.866,0.5))
    G1.add_node(5, pos=(2.732,1))
    G1.add_node(6, pos=(2.732,0))
    E = [[1,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,6]]
    G1.add_edges_from(E)
    G1_node_labels = {node: '$v_{' + str(node) +'}$' for node in G1.nodes()}
    G1_node_positions = nx.get_node_attributes(G1,'pos')

    G1_options = {
        'pos': G1_node_positions,
        'with_labels': True, 
        'labels': G1_node_labels,
        'node_color':'plum',
        'node_size':300
    }

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(60, 30))
    ax1, ax2, ax3, ax4 = axes.flatten()

    nx.draw(G1, ax=ax1, **G1_options)
    ax1.set_title('$G_1$')

    G2 = nx.Graph()
    G2.add_node(1, pos=(0, 3))
    G2.add_node(2, pos=(2, 3))
    G2.add_node(3, pos=(4, 3))
    G2.add_node(4, pos=(6.5, 3))
    G2.add_node(5, pos=(6.5, 0))
    G2.add_node(6, pos=(4.5, 0))
    G2.add_node(7, pos=(2, 0))
    G2.add_node(8, pos=(0, 0))
    G2.add_node(9, pos=(5, 1.5))
    E = [[1,2],[1,8],[2,3],[2,6],[2,7],[3,4],[3,7],[3,9],
         [4,5],[4,6],[4,9],[5,6],[6,7],[6,8],[6,9],[7,8]]
    G2.add_edges_from(E)
    G2_node_labels = {node: '$v_{' + str(node) +'}$' for node in G2.nodes()}
    G2_node_positions = nx.get_node_attributes(G2,'pos')

    G2_options = {
        'pos': G2_node_positions,
        'with_labels': True, 
        'labels': G2_node_labels,
        'node_color':'plum',
        'node_size':300
    }

    

    # draw the whole graph without the edgeS (4,6) and (6,8)
    #  which will be drawn as a custom curved line
    edge_list = list(G2.edges())
    edge_list.remove((4,6))
    edge_list.remove((6,8))
    nx.draw(G2, edgelist=edge_list,ax=ax2, **G2_options)
    ax2.set_title('$G_2$')

    # Draw the edge between nodes 4 and 6 with a curved line
    ax2.annotate("",
                xy=G2_node_positions[4], xycoords='data',
                xytext=G2_node_positions[6], textcoords='data',
                arrowprops=dict(arrowstyle="-", color="black",
                                shrinkA=9, shrinkB=9,
                                patchA=None, patchB=None,
                                connectionstyle="arc",
                                )
                )

    plt.show()

if __name__ == '__main__':
    
    paths_exercise1()
    check_if_biconnected_find_cut_points_exercise2()
    find_partition_exercise3()
    check_if_euler_exercise4()
