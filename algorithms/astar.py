from heapq import *

def heuristic(v1, v2):
    return 0


def astar(graph, start, end):
    queue = []
    heappush(queue, (0, start))
    current_cost = {start: 0}
    path = {start: 0}
    goal_reached = False

    while len(queue) > 0:
        current = heappop(queue)[1]

        if current == end and len(current_cost) == graph.num_nodes:
            goal_reached = True
            break

        for next_node in graph.neighbors(current):
            new_cost = current_cost[current] + graph.edge_cost(current, next_node)
            if next_node not in current_cost or new_cost < current_cost[next_node]:
                current_cost[next_node] = new_cost
                priority = new_cost + heuristic(current, next_node)
                heappush(queue, (priority, next_node))
                path[next_node] = current
    print(get_path(path, start, end))
    return current_cost


def get_path(path, start, end):
    ret = []
    current = end
    while current != start:
        ret.append(current)
        current = path[current]

    ret.append(start)
    ret.reverse()
    return ret

