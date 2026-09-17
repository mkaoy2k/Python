from pyvis.network import Network
import webbrowser
import os

net = Network(height="600px", width="100%", bgcolor="#111111", font_color="white", directed=True)

# Configure hover options to show titles and arrow settings
net.set_options("""
{
  "interaction": {
    "hover": true,
    "tooltipDelay": 200
  },
  "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 3
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
    }
  }
}
""")

net.add_node(
    1,
    label="Python\npyvis\ninteractive graph",
    title="Python stack - hover to see this tooltip",
    color="#3776AB",
    size=30,
    shape="box",
    font={"align": "center", "size": 32, "color": "white", "face": "Arial", "bold": True},
)

net.add_node(
    2,
    label="NetworkX\ngraph data",
    color="#10B981",
    size=12,
    shape="box",
    font={"align": "center", "size": 32, "color": "white", "face": "Arial"},
)

net.add_edge(1, 2, arrow_straight=True, arrows='to')

# Save the interactive graph
html_file = "sample/my_bold_1st_line.html"
net.save_graph(html_file)

# Get absolute path and open in browser
abs_path = os.path.abspath(html_file)
print(f"Graph saved to: {abs_path}")
print("Opening in browser...")

# Open the HTML file in the default web browser
webbrowser.open(f"file://{abs_path}")