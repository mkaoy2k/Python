from graphviz import Digraph

dot = Digraph('graphEx5', format='png')

# Same rank for A and B
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('A')
    s.node('B')

dot.node('C')
dot.edge('A', 'C', constraint='false')  # A->C doesn't affect ranking
dot.edge('B', 'C', weight='10')         # Stronger edge

dot.render('sample/graphEx5.gv', view=True)
