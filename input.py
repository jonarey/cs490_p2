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

#    def add_node(self, node):
#        new_n = Node(node)  # create a new node
#        self.nodes.append(new_n)  # add the node to the list

    def add_edge(self, start, end):
        # add both nodes to the list of edges for each node
        self.graph[start].append(end)

    def dfs_travel(self,start,visited):
        #mark curr as visited
        print start,
        visited[start] = True
        print start,
        for i in self.graph[start]:
            #if not visited search 
            if visited[i] == False:
                self.dfs_travel(i,visited)

    def dfs(self,start):
        #create array of false visited for graph
        visited = [False]*(len(self.graph))
        self.dfs_travel(start,visited)

def read_input():
    inputstr = "SampleDataset1/SampleDataset1.json"  # init str
    in_file = open(inputstr, 'r')

    json_data = json.load(in_file)  # load in the json

    for item in json_data['controllers']:
        controllers.append((item['assetGroupName'], item['globalId'],
                            item['geometry']['x'], item['geometry']['y']))


# read_input()

# create the graph
json_graph = Graph()

infile = open("SampleDataset1/SampleDataset1.json", 'r')
stuff = json.load(infile)
for row in stuff['rows']:
    # add the edges
    # new_edge = Edge(row['viaGlobalId'], row['fromGlobalId'], row['toGlobalId'])
    json_graph.add_edge(row['fromGlobalId'], row['toGlobalId'])
    # new_edge.end = row['toGlobalId']
    # new_edge.start = row['fromGlobalId']
    #graph.add_edge(new_edge)
    print(row['fromGlobalId'] + " " + row['toGlobalId'])
    #print(new_edge.val + " " + new_edge.startid + " " + new_edge.endid)
json_graph.dfs('155BC438-029D-464E-83CF-6D7898C1AE05')
#json_graph.dfs('B6FA6D95-13A4-48BE-8712-A6C3068DDF57')
