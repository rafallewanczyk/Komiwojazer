from pygraph import graph_to_dot
from pygraph.classes.undirected_graph  import UndirectedGraph
from heapq import *
class Astar:
   search_space = UndirectedGraph()
   final_cost = 0
   result = []
   
   def is_on_path(self, path, v1, v2):
      if abs(path.index(v1) - path.index(v2)) == 1:
         return 1
      else:
         return 0

   def heuristic(self, graph, path,  v1, v2):
      l = sorted(list(graph.get_all_edge_objects()), key = lambda x : x['cost'])
      for i in l:
         if self.is_on_path(path, i['vertices'][0], i['vertices'][1]):
            continue
         else :
            return l['cost'] * (graph.num_nodes() - len(path))
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
         print(f"biore {id}' ")
         print(self.search_space.nodes[id]['data']['path'])
         for v in graph.neighbors(self.search_space.nodes[id]['data']['path'][-1]):
            if v in self.search_space.nodes[id]['data']['path']:
               continue

            if len(self.search_space.nodes[id]['data']['path']) == graph.num_nodes():
               print(f"{self.search_space.nodes[id]['data']['path']} koszt : {self.search_space.nodes[id]['data']['cost']}")
               return

            new = self.search_space.new_node()
            self.search_space.nodes[new]['data']['path'] = self.search_space.nodes[id]['data']['path']  + [v]
            self.search_space.new_edge(new, id, graph.edge_cost(v, self.search_space.nodes[id]['data']['path'][-1]) + self.heuristic(graph, self.search_space.nodes[id]['data']['path'], v, self.search_space.nodes[id]['data']['path'][-1]))
            self.search_space.nodes[new]['data']['cost'] = self.search_space.nodes[id]['data']['cost'] + graph.edge_cost(v, self.search_space.nodes[id]['data']['path'][-1])
            print(f"dodaje {v} ")
            print(self.search_space.nodes[new]['data']['path'])
            heappush(queue, (self.search_space.nodes[new]['data']['cost'], new))
         print("___________________")
         #visited.append(queue.pop(0))


      print(graph_to_dot(self.search_space))
