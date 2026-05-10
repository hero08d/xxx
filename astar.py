def astar(start, goal):
    open_list = [start]
    g = {start: 0}
    parent = {start: None}

    while open_list:
        # pick best node (minimum g + h)
        current = open_list[0]
        for node in open_list:
            if g[node] + h(node) < g[current] + h(current):
                current = node

        # goal reached
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            print(path[::-1])
            return

        open_list.remove(current)

        # explore neighbours
        for neighbour, cost in graph[current]:
            new_cost = g[current] + cost

            if neighbour not in g or new_cost < g[neighbour]:
                g[neighbour] = new_cost
                parent[neighbour] = current
                open_list.append(neighbour)

    print("No path")


# graph
graph = {
    'A': [('B',1), ('C',3), ('D',7)],
    'B': [('D',5)],
    'C': [('D',12)],
    'D': []
}

# heuristic
def h(n):
    H = {'A':11, 'B':6, 'C':99, 'D':1}
    return H[n]

astar('A', 'D')
