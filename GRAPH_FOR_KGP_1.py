import networkx as nx 
import matplotlib.pyplot as plt 
  
g = nx.Graph() 
for i in range(24):
    if i%3==0:
        g.add_edge(i,i+1)
        g.add_edge(i,i+2)
    if i%3==1:
        g.add_edge(i,i-1)
        g.add_edge(i,i+1)
    if i%3==2:
        g.add_edge(i,i-1)
        g.add_edge(i,i-2)


g.add_edges_from([(5,10),(13,18)])
nx.draw_circular(g,node_size = 40,edge_color = ['red' if e[0]==5 or e[0]==10 or e[0]==13 or e[0]==18 or e[1]==5 or e[1]==10 or e[1]==13 or e[1]==18 else 'green' for e in g.edges]) 
plt.savefig("filename1.png")
plt.show()
