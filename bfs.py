from collections import deque

def bfs():
    visited = set()
    q = deque()
    
    q.append((0, 0))
    visited.add((0, 0))
    
    while q:
        x, y = q.popleft()
        print(x, y)
        
        if x == 2 or y == 2:
            print("Goal reached")
            return
        
        moves = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (max(0, x-(3-y)), min(3, y+x)),
            (min(4, x+y), max(0, y-(4-x)))
        ]
        
        for m in moves:
            if m not in visited:
                q.append(m)
                visited.add(m)

bfs()
