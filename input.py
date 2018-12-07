# date:     11/22/2018
# purpose:  for reading and storing the input data

import json
import sys
from collections import defaultdict

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
        self.graph = defaultdict(list)
        self.curr_index = -1
#    def add_node(self, node):
#        new_n = Node(node)  # create a new node
#        self.nodes.append(new_n)  # add the node to the list

    def add_edge(self, start, end):
        # add both nodes to the list of edges for each node
        self.graph[start].append(end)

# finds the index of the input key
    def find_index(self, key):
        i = 0
        for node_id in self.graph:
            if key == node_id:
                self.curr_index = i
                # print i,
            else:
                i += 1

    def dfs_travel(self, start, visited):

        # finds index of node
        self.find_index(start)
        visited[self.curr_index] = True
        print start,
        for i in self.graph[start]:
            # if not visited search
            self.find_index(i)
            if visited[self.curr_index] == False:
                self.dfs_travel(i, visited)

    def dfs(self, start):
        # create array of false visited for graph
        visited = [False]*(len(self.graph))
        self.dfs_travel(start, visited)


def read_input():
    inputstr = "SampleDataset1/SampleDataset1.json"  # init str
    in_file = open(inputstr, 'r')

    json_data = json.load(in_file)  # load in the json

    for item in json_data['controllers']:
        controllers.append((item['assetGroupName'], item['globalId'],
                            item['geometry']['x'], item['geometry']['y']))

# cmd line inputs
json_file = ""
start_file = ""
if len(sys.argv) < 3:
    print("Please provide 2 files: a json file for input, and a text file with starting points")
    print("Usage: python2 input.py input.json startpoints.txt")
    exit(2)
else:
    json_file = sys.argv[1]
    start_file = sys.argv[2]

try:
    infile = open(json_file, 'r')
except:
    print("Please correct the path to the JSON file.")
    exit(3)

# get the start node
start_point = ""
try:
    with open(start_file, 'r') as f:
        start_point = f.readline()  # get the first line
    start_point.strip()  # clean it
except:
    print("Please enter a valid path to the text file.")
    exit(4)

# create the graph
json_graph = Graph()
stuff = json.load(infile)
for row in stuff['rows']:
    # add the edges
    # new_edge = Edge(row['viaGlobalId'], row['fromGlobalId'], row['toGlobalId'])
    json_graph.add_edge(row['fromGlobalId'], row['toGlobalId'])
    # new_edge.end = row['toGlobalId']
    # new_edge.start = row['fromGlobalId']
    # graph.add_edge(new_edge)
    # print(row['fromGlobalId'] + " " + row['toGlobalId'])
    # print(new_edge.val + " " + new_edge.startid + " " + new_edge.endid)

print("Upstream Path (DFS)")
json_graph.dfs("{" + start_point + "}")
json_graph.find_index('{B6FA6D95-13A4-48BE-8712-A6C3068DDF57}')
