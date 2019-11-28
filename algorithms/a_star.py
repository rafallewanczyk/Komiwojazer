from pygraph import graph_to_dot
from pygraph.classes.undirected_graph  import UndirectedGraph
from heapq import *
class Astar:
   search_space = UndirectedGraph()
   final_cost = 0
   result = list()
   queue = []

   def heuristic(self, v1, v2):
      return 0

   def run(self, graph, start):
      self.a_star(graph, start)

   def a_star(self, graph, start):
      queue = []
      heappush(queue, (0, start))
      current_cost = {start: 0}
      path = {start: 0}
      goal_reached = False

      while len(queue) > 0:
         current = heappop(queue)[1]

         # if current == end and len(current_cost) == graph.num_nodes:
         #    goal_reached = True
         #    break

         self.search_space.new_node_id(current)

         for next_node in graph.neighbors(current):
            new_cost = current_cost[current] + graph.edge_cost(current, next_node)
            if next_node not in current_cost or new_cost < current_cost[next_node]:
               current_cost[next_node] = new_cost
               priority = new_cost + self.heuristic(current, next_node)
               heappush(queue, (priority, next_node))
               self.search_space.new_node_id(next_node)
               self.search_space.new_edge(current, next_node, priority)
               path[next_node] = current
      print(graph_to_dot(self.search_space))
      return current_cost

   def generate_search_space(self, graph, start):
      id = self.search_space.new_node()
      self.search_space.nodes[id]['data'] = [start]

      queue = []
      visited = []
      queue.append(id)

      while len(queue) > 0:
         print(queue)
         print(visited)
         id = queue.pop(0)
         print("biore %i'" %id, end=" ")
         print(self.search_space.nodes[id]['data'])
         for v in graph.neighbors(self.search_space.nodes[id]['data'][-1]):
            if(v in self.search_space.nodes[id]['data']): continue
            new = self.search_space.new_node()
            self.search_space.new_edge(new, id, graph.edge_cost(v, self.search_space.nodes[id]['data'][-1]))
            self.search_space.nodes[new]['data'] = self.search_space.nodes[id]['data']  + [v]
            print("dodaje %i" %v, end=" ")
            print(self.search_space.nodes[new]['data'])
            queue.append(new)

         print("___________________")
         #visited.append(queue.pop(0))


      print(graph_to_dot(self.search_space))
