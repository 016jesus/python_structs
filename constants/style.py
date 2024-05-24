
#estilos definidos al programa
windowSize = "1300x800"
backgroundColor = "#0A1B0E"
node_color = 'w'
edge_color = "#7ED130"
titulo = "Proyecto Estructuras de datos"
file = "grafo_villavo.pkl"
font = "Bahnschrift"
verdelimaOscuro = "#172907"
negroBotones = "#1F1F1A"

def style_unvisited_edge(G, edge):        
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(G, edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_active_edge(G, edge):
    G.edges[edge]["color"] = '#e8a900'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_path_edge(G, edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1