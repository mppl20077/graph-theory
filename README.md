# graph-theory

For nx.drawing.nx_agraph.graphviz_layout to work in windows we need
to download  https://www.graphviz.org/download/ and add its bin to the
PATH. Then we need to install it via

pip install --global-option=build_ext --global-option="-IC:\Program Files\Graphviz\include" --global-option="-LC:\Program Files\Graphviz\lib" pygraphviz