#!/usr/bin/env python
"""Tarjan's Algorithm 
give file name as the first argument """
import sys
def scc(graph):

    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    final_components = []
    
    def strongconnect(node):
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
    
        try:
            successors = graph[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowlinks:
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node],lowlinks[successor])
            elif successor in stack:
                lowlinks[node] = min(lowlinks[node],index[successor])
        
        if lowlinks[node] == index[node]:
            connected_component = []
            
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            component = tuple(connected_component)
            final_components.append(component)
    
    for node in graph:
        if node not in lowlinks:
            strongconnect(node)
    
    return final_components



if __name__ == '__main__':
    graph = {}
    with open(sys.argv[1]) as f: 
        for line in f:
            t = line.strip().split()
            try:
                graph[t[0]].append(t[1]) 
            except Exception, e:
                graph[t[0]] = [t[1]]
    print len(scc(graph))