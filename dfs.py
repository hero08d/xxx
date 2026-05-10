def dfs(x, y, visited, path):
    if (x, y) in visited:
        return
    
    visited.add((x, y))
    path.append((x, y))   # add current state to path
    
    if x == 2 or y == 2:
        print("Path:")
        for p in path:
            print(p)
        print("Goal reached")
        return
    
    # explore all moves
    dfs(4, y, visited, path)
    dfs(x, 3, visited, path)
    dfs(0, y, visited, path)
    dfs(x, 0, visited, path)
    dfs(max(0, x-(3-y)), min(3, y+x), visited, path)
    dfs(min(4, x+y), max(0, y-(4-x)), visited, path)
    
    path.pop()  # backtrack

dfs(0, 0, set(), [])
