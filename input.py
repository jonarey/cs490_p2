# date:     11/22/2018
# purpose:  for reading and storing the input data

import json
import sys

controllers = []


class Node:
    def __init__(self, val):
        self.val
        self.edges = []


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes  # init a list of nodes

    def add_node(self, node):
        new_n = Node(node)  # create a new node
        self.nodes.append(new_n)  # add the node to the list

    def add_edge(self, n1, n2):
        # add both nodes to the list of edges for each node
        n1.edges.append(n2)
        n2.edges.append(n1)


def read_input():
    inputstr = ""  # init str
    with open("SampleDataset1/SampleDataset1.json", 'r') as file:
        inputstr = file.read()  # read in the file

    json_str = json.load(inputstr)  # load in the json

    for item in json_str['controllers']:
        controllers.append((item['assetGroupName'], item['globalId'],
                            item['geometry']['x'], item['geometry']['y']))


read_input()

# create the graph
graph = Graph()

for row in json_str['rows']:
    # add the node
    node_one = row['toGlobalId']
    node_two = row['fromGlobalId']
    graph.add_node(node_one, node_two)

    # add the edges
    edges = row['viaGeometry']
    edges = edges.get('paths')
    if edges != None:
        edges = edges[0]
        edges = [g.add_edge(x[0], x[1]) for x in edges]
