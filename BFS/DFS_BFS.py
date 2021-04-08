from collections import deque
from copy import deepcopy

#! DFS : recusively
#! BFS : deque

# use deepcopy
def DFS(G, state, visited):
    print(f"{state}", end=' ')
    visited = deepcopy(visited)
    visited[state] = True
    
    sub_level = G[state-1]
    if len(sub_level) > 0:
        for pos in sub_level:
            if not visited[pos]:
                visited = DFS(G, pos, visited)
        return visited

# use same list
def DFS(G, state, visited):
    print(f"{state}", end=' ')
    visited[state] = True
    
    sub_level = G[state-1]
    if len(sub_level) > 0:
        for pos in sub_level:
            if not visited[pos]:
                DFS(G, pos, visited)
        return

# use deque
def BFS(G, state, visited):
    que = deque([state])
    
    while que:
        state = que.popleft()
        if not visited[state]:
            print(f"{state}", end= ' ')
            visited[state] = True
        
            if len(G[state-1]) > 0:
                for pos in G[state-1]:
                    if not visited[pos]:
                        que.append(pos)
    
    return

if __name__ == '__main__':
    graph = [
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]
        
    start = 1
    
    visited = [False for _ in range(len(graph)+1)]
    DFS(G=graph, state=start, visited=visited)
    print("")
    
    visited = [False for _ in range(len(graph)+1)]
    BFS(G=graph, state=start, visited=visited)





