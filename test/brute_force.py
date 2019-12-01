import unittest
from math import sqrt
from data.graph_manager import GraphManager
from algorithms.brute_force import BruteForce

class BruteForceTest(unittest.TestCase):

    graph_manager = GraphManager()

    def test_solve(self):
        graph = self.graph_manager.read_from_file("test/test1_nodes.txt", "test/test1_links.txt")

        self.assertListEqual(BruteForce().solve(graph, "B")[0], [])
        self.assertListEqual(BruteForce().solve(graph, "A")[0], ["A", "B", "C", "D"])



if __name__ == "__main__":
    unittest.main()