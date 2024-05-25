
#estilos definidos al programa
windowSize = "1300x800"
backgroundColor = "#80c9b8" # gris medio oscurito jeje xd
main = "#98e1d0"

node_color = 'w'
edge_color = "black" #verde clarito
titulo = "Proyecto Estructuras de datos"
file = "grafo_villavo.pkl"
font = "Bahnschrift"
verdelimaOscuro = "#172907" 
negroBotones = "#1F1F1A"








def unvisited_edge(G, edge):        
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def visited_edge(G, edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def active_edge(G, edge):
    G.edges[edge]["color"] = '#e8a900'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def path_edge(G, edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1] = 1
    G.edges[edge]["linewidth"] = 1
