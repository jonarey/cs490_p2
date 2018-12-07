# date:     11/22/2018
# purpose:  for reading and storing the input data

import json
import sys

controllers = []
json_data = ""


class Node:
    def __init__(self, val):
        self.val
        self.edges = []


class Edge:
    def __init__(self, val, startid, endid):
        self.val = val
        self.startid = startid
        self.endid = endid


class Graph:
    def __init__(self, edges=[]):
        self.edges = edges  # init a list of nodes

    def add_node(self, node):
        new_n = Node(node)  # create a new node
        self.nodes.append(new_n)  # add the node to the list

    def add_edge(self, new_e):
        # add both nodes to the list of edges for each node
        self.edges.append(new_e)
        #n2.edges.append(n1)


def read_input():
    inputstr = "SampleDataset1/SampleDataset1.json"  # init str
    in_file = open(inputstr, 'r')

    json_data = json.load(in_file)  # load in the json

    for item in json_data['controllers']:
        controllers.append((item['assetGroupName'], item['globalId'],
                            item['geometry']['x'], item['geometry']['y']))


# read_input()

# create the graph
graph = Graph()

infile = open("SampleDataset1/SampleDataset1.json", 'r')
stuff = json.load(infile)
for row in stuff['rows']:
    # add the edges
    new_edge = Edge(row['viaGlobalId'],row['fromGlobalId'],row['toGlobalId'])
    #new_edge.end = row['toGlobalId']
    #new_edge.start = row['fromGlobalId']
    graph.add_edge(new_edge)
    print(new_edge.val + " " + new_edge.startid + " " + new_edge.endid)

