class BruteForce:
    final_cost = float("inf")
    result = list()
    visited = list()

    def brute(self, graph, start, cost = 0):
        self.visited.append(start)
        for vert in graph.neighbors(start):
            if vert not in self.visited:
                cost += graph.edge_cost(vert, start)
                self.brute(graph, vert, cost)

        if len(self.visited) == graph.num_nodes() and cost < self.final_cost :
                self.final_cost = cost
                self.result = self.visited.copy()

        self.visited.pop()

    def run(self, graph, start, cost = 0):
       self.brute(graph, start, cost)
       print(self.result)
       print(self.final_cost)
       return cost