from pygraph import graph_to_dot
from pygraph.classes.undirected_graph  import UndirectedGraph
from heapq import *
class Astar:
   search_space = UndirectedGraph()
   final_cost = 0
   result = []
   

   def heuristic(self, v1, v2):
      return 0

   


   def generate_search_space(self, graph, start):
      id = self.search_space.new_node()
      self.search_space.nodes[id]['data'] = {'path' : [start], 'cost' : 0}

      queue = []
      #queue.append(id)
      heappush(queue, (0, start))

      while len(queue) > 0:
         print(queue)

         id = heappop(queue)[1]
         print("biore %i'" %id, end=" ")
         print(f"biore {id} ")
         print(self.search_space.nodes[id]['data']['path'])
         for v in graph.neighbors(self.search_space.nodes[id]['data']['path'][-1]):
            if v in self.search_space.nodes[id]['data']['path']:
               continue

            new = self.search_space.new_node()
            self.search_space.new_edge(new, id, graph.edge_cost(v, self.search_space.nodes[id]['data']['path'][-1]))
            self.search_space.nodes[new]['data']['path'] = self.search_space.nodes[id]['data']['path']  + [v]
            self.search_space.nodes[new]['data']['cost'] = self.search_space.nodes[id]['data']['cost'] + graph.edge_cost(v, self.search_space.nodes[id]['data']['path'][-1])
            print(f"dodaje {v} ")
            print(self.search_space.nodes[new]['data']['path'])
            heappush(queue, (0, new))#ToDo
         print("___________________")
         #visited.append(queue.pop(0))


      print(graph_to_dot(self.search_space))
