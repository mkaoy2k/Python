from pyvis.network import Network
import networkx as nx
import webbrowser
import os

# Optional: create a graph with NetworkX first (very common pattern)
G = nx.DiGraph()
G.add_edges_from([
    ("Python", "NetworkX"),
    ("Python", "Pyvis"),
    ("NetworkX", "Graph Analysis"),
    ("Pyvis", "Interactive Viz"),
    ("Graph Analysis", "Insights"),
    ("Interactive Viz", "Insights"),
    ("Python", "Matplotlib"),
    ("Matplotlib", "Static Viz")
])

# Create the interactive network
net = Network(
    height="750px",
    width="100%",
    bgcolor="#222222",
    font_color="white",
    directed=True,          # set to False for undirected
    notebook=False          # set True if running in Jupyter
)

# Load the NetworkX graph into Pyvis
net.from_nx(G)

# Optional but recommended: nicer physics & styling
net.set_options("""
{
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -50,
      "centralGravity": 0.01,
      "springLength": 100,
      "springConstant": 0.08
    },
    "minVelocity": 0.75,
    "solver": "forceAtlas2Based"
  },
  "nodes": {
    "shape": "dot",
    "size": 25,
    "font": {
      "size": 18,
      "face": "Tahoma"
    }
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 0.8
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": {
      "type": "continuous"
    }
  }
}
""")

# Save the interactive graph
html_file = "sample/my_graph.html"
net.save_graph(html_file)

# Get absolute path and open in browser
abs_path = os.path.abspath(html_file)
print(f"Graph saved to: {abs_path}")
print("Opening in browser...")

# Open the HTML file in the default web browser
webbrowser.open(f"file://{abs_path}")