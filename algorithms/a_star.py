import networkx as net
import matplotlib.pyplot as plt
from heapq import *


class Astar:
    search_space = net.Graph()
    visited_states = 1
    l = []

    def is_on_path(self, path, v1, v2):
        try:
            if abs(path.index(v1) - path.index(v2)) == 1:
                return 1
            else:
                return 0

        except ValueError:
            return 0

    def shortes_from_all_heuristic(self, graph, path):

        for i in self.l:
            if self.is_on_path(path, i[0], i[1]):
                continue
            else:
                return i[2] * (graph.number_of_nodes() - len(path))
        return 0

    def greedy_heuristic(self, graph, path, v):
        min = float("inf")
        for i in graph.neighbors(v):
            if graph.get_edge_data(v, i)['weight'] < min : min = graph.get_edge_data(v, i)['weight']
        return min * (graph.number_of_nodes() - len(path))


    def solve(self, graph, start, heuristic="z"):
        self.l = sorted(graph.edges(data="weight"), key=lambda x: x[2])
        index = 1
        self.search_space.add_node(index)
        self.search_space.nodes[index]['path'] = [start]
        self.search_space.nodes[index]['cost'] = 0
        self.search_space.nodes[index]['h'] = 0

        queue = []
        heappush(queue, (self.search_space.nodes[index]['h'] + self.search_space.nodes[index]['cost'], index))
        index += 1

        while len(queue) > 0:
            current = heappop(queue)[1]
            current_node = self.search_space.nodes[current]
            if len(current_node['path']) == graph.number_of_nodes():
                return current_node['path'], current_node['cost'], self.visited_states

            last_on_path = self.search_space.nodes[current]['path'][-1]
            for v in list(graph.neighbors(last_on_path)):
                if v in current_node['path']:
                    continue

                self.visited_states += 1
                if self.visited_states % 100000 == 0:
                    print(self.visited_states)
                    
                self.search_space.add_node(index)
                new = index
                index += 1

                new_node = self.search_space.nodes[new]

                new_node['path'] = current_node['path'] + [v]
                self.search_space.add_edge(current, new,
                                           weight=graph.get_edge_data(v, last_on_path)['weight'])

                new_node['cost'] = current_node['cost'] + \
                                   graph.get_edge_data(v, last_on_path)['weight']
                if heuristic == 'z':
                    new_node['h'] = 0
                elif heuristic == 'g':
                    new_node['h'] = self.greedy_heuristic(graph, self.search_space.nodes[new]['path'], v)
                else:
                    new_node['h'] = self.shortes_from_all_heuristic(graph, self.search_space.nodes[new]['path'])

                heappush(queue, (new_node['h'] + new_node['cost'], new))

        return [], 0, self.visited_states
