# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:06:03 2019

@author: josep
"""

import random
random.seed(1)
def subsetFinder(graph): # Graph in form [[x] for x in superset]. [x] here is called a "section"
    if not len(graph): 
        return []
    elif len(graph) == 1:
        return graph[0]
    
    parser_1 = 0 # IDEA: merge sections whenever at least one element in 
    parser_2 = 0 #section 1 divides at least one element in section 2
    
    while parser_1 < len(graph) - 1:
        current_segment = graph[parser_1]
        parser_2 = parser_1 + 1
        while parser_2 < len(graph):
            other_segment = graph[parser_2];breakFlag = False
            for num_1 in current_segment:
                for num_2 in other_segment:
                    if not (num_1 % num_2 and num_2 % num_1):
                        current_segment.extend(other_segment)
                        graph.pop(parser_2)
                        breakFlag = True
                        break
                if breakFlag:
                    break
            if not breakFlag:
                parser_2 += 1
        parser_1 += 1 
    return max(graph, key=len)
    
import timeit
def main():
    n_max= 50
    for n in range(n_max):
        startingSet = [random.randint(1, 10) for dummy in range(n)]
        graph = [[num] for num in startingSet]
        a = lambda : subsetFinder(graph)
        print(timeit.timeit(a, number=10000))
        
main()
#startingSet = [2, 4, 7, 6,4,8,8, 7, 13, 7*13, 7*5, 5, 77, 777]
#graph = [[num] for num in startingSet]

#print(graph)
#print(subsetFinder(graph))

'''


for idx_1, connected_segment in enumerate(graph[:]):
    for num_1 in connected_segment:
        for idx_2, other_segment in enumerate(graph):
            for num_2 in other_segment:
                if not num_1 % num_2 or not num_2 % num_1:
                    graph[idx_1].update(other_segment)
                    graph.remove(idx_2 + deleted)
                    deleted += 1
                    continue
print(graph)
print(max(graph, key=len))
                
'''        
print(startingSet)