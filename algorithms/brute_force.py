class BruteForce:
    final_cost = float("inf")
    result = []
    visited = []
    visited_states = 0

    def brute(self, graph, start, cost = 0):
        self.visited.append(start)
        self.visited_states += 1

        for vert in graph.neighbors(start):
            if vert not in self.visited:
                self.brute(graph, vert, cost + graph.get_edge_data(vert, start)['weight'])

        if len(self.visited) == graph.number_of_nodes() and cost < self.final_cost :
                self.final_cost = cost
                self.result = self.visited.copy()
        self.visited.pop()

    def solve(self, graph, start, cost = 0):
       self.brute(graph, start)
       
       return self.result, self.final_cost, self.visited_states