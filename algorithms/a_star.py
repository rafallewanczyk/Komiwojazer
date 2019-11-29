import networkx as net
import matplotlib.pyplot as plt
from heapq import *


class Astar:
    search_space = net.Graph()
    final_cost = 0
    result = []

    def is_on_path(self, path, v1, v2):
        try:
            if abs(path.index(v1) - path.index(v2)) == 1:
                return 1
            else:
                return 0

        except ValueError:
            return 0

    def heuristic(self, graph, path):
        l = sorted(graph.edges(data="weight"), key=lambda x: x[2])
        for i in l:
            if self.is_on_path(path, i[0], i[1]):
                continue
            else:
                return i[2] * (graph.number_of_nodes() - len(path))
        return 0

    def solve(self, graph, start):
        index = 1
        self.search_space.add_node(index)
        self.search_space.nodes[index]['path'] = [start]
        self.search_space.nodes[index]['cost'] = 0
        self.search_space.nodes[index]['h'] = self.heuristic(graph, self.search_space.nodes[index]['path'])

        queue = []
        heappush(queue, (self.search_space.nodes[index]['h'] + self.search_space.nodes[index]['cost'], index))
        index += 1

        while len(queue) > 0:
            current = heappop(queue)[1]

            print(f"biore {current}' ")
            print(self.search_space.nodes[current]['path'])

            last_on_path = self.search_space.nodes[current]['path'][-1]
            for v in list(graph.neighbors(last_on_path)):

                if len(self.search_space.nodes[current]['path']) == graph.number_of_nodes():
                    print(
                        f"{self.search_space.nodes[current]['path']} koszt : {self.search_space.nodes[current]['cost']}")
                    for i in range(1, self.search_space.number_of_nodes() + 1):
                        print(f"{i}", end=" : ")
                        print(self.search_space.nodes[i]['path'])
                    net.draw_networkx(self.search_space)
                    plt.show()

                    return

                if v in self.search_space.nodes[current]['path']:
                    continue

                self.search_space.add_node(index)
                new = index
                index += 1

                self.search_space.nodes[new]['path'] = self.search_space.nodes[current]['path'] + [v]
                self.search_space.add_edge(current, new,
                                           weight=graph.get_edge_data(v, last_on_path)['weight'])

                self.search_space.nodes[new]['cost'] = self.search_space.nodes[current]['cost'] + \
                                                       graph.get_edge_data(v, last_on_path)['weight']
                self.search_space.nodes[new]['h'] = self.heuristic(graph, self.search_space.nodes[new]['path'])

                print(f"dodaje {v} ")
                print(self.search_space.nodes[new]['path'], end=" ")
                print(self.search_space.nodes[new]['h'] + self.search_space.nodes[new]['cost'])
                heappush(queue, (self.search_space.nodes[new]['h'] + self.search_space.nodes[new]['cost'], new))
            print("___________________")

        for i in range(1, self.search_space.number_of_nodes() + 1):
            print(f"{i}", end=" : ")
            print(self.search_space.nodes[i]['path'])
        net.draw_networkx(self.search_space)
        plt.show()
