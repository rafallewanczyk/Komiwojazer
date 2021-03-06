import networkx as net
from data.graph_manager import GraphManager
from data.graph_drawer import GraphDrawer
from algorithms.brute_force import BruteForce
from algorithms.a_star import Astar
import argparse
from time import time


def main():
    parser = argparse.ArgumentParser(description="Program finds shortest hamilton's path in graph")
    parser.add_argument("nodesfile", type=str, help="Graph nodes file to import")
    parser.add_argument("linksfile", type=str, help="Graph links file to import")
    parser.add_argument("firstnode", type=str, help="Node where algorithms start")
    parser.add_argument("-b", "--brute", action="store_true", help="Execute brute algorithm")
    parser.add_argument("-a", "--astar", action="store_true", help="Execute astar algorithm")
    parser.add_argument("-w", "--write", type=str, help="Write results to text file")
    parser.add_argument("-f", "--function", help="Choice of heuristic (g - greedy, s - shortest, z - zero (default))")
    parser.add_argument("-d", "--draw", type=str, help="Draw a graph with found path (b from brute, a from astar)")
    args = parser.parse_args()

    manager = GraphManager()
    drawer = GraphDrawer()
    
    graph = manager.read_from_file(args.nodesfile, args.linksfile)

    if args.brute:
        start = time()
        brute_results = BruteForce().solve(graph, args.firstnode)
        end = time()
        total_time = end - start
        print("Brute force:")
        print(f"Path: {brute_results[0]}")
        print(f"Cost: {brute_results[1]} Visited states: {brute_results[2]}")
        print(f"Time: {total_time} s")
        print("_______________________")
        if args.write is not None:
            with open(args.write, "a") as f:
                f.write(f"Brute force:\nPath: {brute_results[0]}\n\
                    Cost: {brute_results[1]} Visited states: {brute_results[2]}\nTime: {total_time} s\n")
        if args.draw == "b":
            path = manager.nodes_path_to_edges(brute_results[0])
            drawer.draw_with_path(graph, path)
    
    if args.astar:
        if args.function == None:
            start = time()
            astar_results = Astar().solve(graph, args.firstnode)
            end = time()
            total_time = end - start
        else:
            start = time()
            astar_results = Astar().solve(graph, args.firstnode, args.function)
            end = time()
            total_time = end - start
        print("Astar:")
        print(f"Path: {astar_results[0]}")
        print(f"Cost: {astar_results[1]} Visited states: {astar_results[2]}")
        print(f"Time: {total_time} s")
        print("_______________________")
        if args.write is not None:
            with open(args.write, "a") as f:
                f.write(f"Astar ({args.function}):\nPath: {astar_results[0]}\n\
                    Cost: {astar_results[1]} Visited states: {astar_results[2]}\nTime: {total_time} s\n")
        if args.draw == "a":
            path = manager.nodes_path_to_edges(astar_results[0])
            drawer.draw_with_path(graph, path)


if __name__ == '__main__':
    main()
