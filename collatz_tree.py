from graphics import *
import networkx as nx
import numpy as np
import math

from collatz import inv_collatz_odd, inv_collatz_even


# initialize graph
G = nx.Graph()

# define parameters for drawing
d_deg = 10
d_rad = math.radians(d_deg)

start_deg = 90
start_rad = math.radians(start_deg)

edge_len = 20

speed = 1000

# add initial nodes
G.add_node(1, o=-1, e=2, x=0, y=0, d=0)

x_coord = edge_len * math.cos(start_rad - d_rad)
y_coord = edge_len * math.sin(start_rad - d_rad)
G.add_node(2, o=-1, e=4, x=x_coord, y=y_coord, d=start_rad - d_rad)

x_coord += edge_len * math.cos(start_rad - 2*d_rad)
y_coord += edge_len * math.sin(start_rad - 2*d_rad)
G.add_node(4, o=1, e=8, x=x_coord, y=y_coord, d=start_rad - 2*d_rad)

x_coord += edge_len * math.cos(start_rad - 3*d_rad)
y_coord += edge_len * math.sin(start_rad - 3*d_rad)
G.add_node(8, o=0, e=0, x=x_coord, y=y_coord, d=start_rad - 3*d_rad)

G.add_edges_from([(1, 2), (2, 4), (1, 4), (4, 8)])

# from the above nodes only 8 is unsaturated
unsat_nodes = np.array([8])

# iterate over numbers
for i in range(2000):
    # get the lowest value unsaturated node
    unsat_nodes = np.sort(unsat_nodes, kind='quicksort')
    curr_n = unsat_nodes[0]

    # if odd inverse collatz hasn't been calculated yet ('o' property is 0)
    if G.nodes[curr_n]['o'] == 0:
        val_o = inv_collatz_odd(curr_n)
        if val_o == -1:
            G.nodes[curr_n]['o'] = val_o
        else:
            G.nodes[curr_n]['o'] = val_o

            # calculate coordinates
            d_angle = G.nodes[curr_n]['d'] + d_rad
            x_coord = G.nodes[curr_n]['x'] + edge_len * math.cos(d_angle)
            y_coord = G.nodes[curr_n]['y'] + edge_len * math.sin(d_angle)

            # add new number to unsaturated nodes list
            unsat_nodes = np.append(unsat_nodes, [val_o])
            G.add_node(val_o, o=0, e=0, x=x_coord, y=y_coord, d=d_angle)
            # add edge between parent and this number
            G.add_edge(curr_n, val_o)

    # if odd inverse collatz hasn't been calculated yet ('e' property is 0)
    if G.nodes[curr_n]['e'] == 0:
        val_e = inv_collatz_even(curr_n)

        G.nodes[curr_n]['e'] = val_e

        # calculate coordinates
        d_angle = G.nodes[curr_n]['d'] - d_rad
        x_coord = G.nodes[curr_n]['x'] + edge_len * math.cos(d_angle)
        y_coord = G.nodes[curr_n]['y'] + edge_len * math.sin(d_angle)

        # add new number to unsaturated nodes list
        unsat_nodes = np.append(unsat_nodes, [val_e])
        G.add_node(val_e, o=0, e=0, x=x_coord, y=y_coord, d=d_angle)
        # add edge between parent and this number
        G.add_edge(curr_n, val_e)

    # remove the now saturated node from the unsaturated node list
    unsat_nodes = np.delete(unsat_nodes, 0)


# draw collatz tree using graphics.py
# initialize window parameters
win_width = 800
win_height = 800

win = GraphWin("Collatz", win_width, win_height, autoflush=False)
win.setBackground("black")

win.setCoords(-win_width*(1/10), -win_height*(7.1/10), win_width*(9/10), win_height*(2.9/10))

# print(G.nodes[8]['e'])
#
# print(G.nodes[G.nodes[8]['e']]['x'])
# wait for mouse
clickPoint = win.getMouse()

# iterate over nodes
for node in list(G):
    x = G.nodes[node]['x']
    y = G.nodes[node]['y']

    r = 255
    g = 255
    b = 255

    # logic for drawing nodes
    if G.nodes[node]['o'] != -1 and G.nodes[node]['o'] != 0:
        xo = G.nodes[G.nodes[node]['o']]['x']
        yo = G.nodes[G.nodes[node]['o']]['y']

        line_o = Line(Point(x, y), Point(xo, yo))
        # line_o.setFill(color_rgb(r, g, b))
        line_o.setFill("white")
        line_o.draw(win)

    if G.nodes[node]['e'] != 0:
        xe = G.nodes[G.nodes[node]['e']]['x']
        # print(xe)
        ye = G.nodes[G.nodes[node]['e']]['y']

        line_e = Line(Point(x, y), Point(xe, ye))
        # line_e.setFill(color_rgb(r, g, b))
        line_e.setFill("white")
        line_e.draw(win)
    update(speed)

# Pause to view result
win.getMouse()
win.close()
