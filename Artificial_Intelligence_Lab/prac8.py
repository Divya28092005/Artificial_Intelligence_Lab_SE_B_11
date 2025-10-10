# Example graph
graph = {
    'Home': {'Bank': 45, 'Garden': 40, 'School': 50},
    'Bank': {'Police Station':60},
    'Garden': {'Railway Station': 72},
    'School': {'Post Office': 59, 'Railway Station': 75},
    'Police Station': {'University': 28},
    'Railway Station':{'University':40},
    'Post office': {},
    'University':{}
}

# Heuristic values
heuristics = {
    'Home': 120, 'Bank': 80, 'Garden': 100, 'School': 70, 'Railway Station': 20, 'Post Office': 110, 'Police Station': 26, 'University': 0
}

import heapq

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, [start]))
    closed_set = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        if node in closed_set:
            continue
        closed_set.add(node)

        for neighbor, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Run A*
start, goal = 'Home', 'University'
path, cost = a_star_search(graph, heuristics, start, goal)
print("Path:", path)
print("Cost:", cost)

