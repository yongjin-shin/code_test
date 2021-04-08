Preparing for the code test

# Problem List
## DFS
1. [19236 청소년 상어](https://www.acmicpc.net/problem/19236)



## BFS

1. [16236 아기 상어](https://www.acmicpc.net/problem/16236)



## Simulation

1. [19237 어른 상어](https://www.acmicpc.net/problem/19237)


# Note
## 1. 최단거리
- BFS, DFS, Dijkstra, Floyd-Warshall
  - E: # of Edges
  - V: # of nodes



### BFS vs Dijkstra
- Dijkstra : 양의 가중치로 모두 다를 때 EO(logV)
- BFS : 모든 가중치가 1로 동일할 때 O(E)
  - collections의 deque를 사용함. 근데 순서가 필요한 경우엔 heapq를 사용한다



## 2. 최대값 (Backtracking)
### DFS vs BFS
- DFS
- BFS : 트리 깊이가 무한대가 될 때. 미로찾기 루프 발생 시.

