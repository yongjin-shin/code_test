Preparing for the code test

# Problem List
## DFS
1. [19236 청소년 상어](https://www.acmicpc.net/problem/19236)
2. [1949 등산로 조성](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq)
윷놀이/backtracking
게리맨더링2

## BFS
1. [16236 아기 상어](https://www.acmicpc.net/problem/16236)
2. [16234 인구이동](https://www.acmicpc.net/problem/16234)
3. [14502 연구소](https://www.acmicpc.net/problem/14502)
4. [17142 연구소3](https://www.acmicpc.net/problem/17142)


이차원배열/loop risk




## Simulation
1. [19237 어른 상어](https://www.acmicpc.net/problem/19237)
2. [20057 토네이도 상어](https://www.acmicpc.net/problem/20057)
원판, 새로운게임2, 낚시왕, 미세먼지, 나무 재테크, 


# Note

## 0. 시간
- N of samples: 1억 ~ 1초

## 1. 최단거리
- BFS, DFS, Dijkstra, Floyd-Warshall
  - E: # of Edges
  - V: # of nodes



### BFS vs Dijkstra
- Dijkstra : 양의 가중치로 모두 다를 때 EO(logV)
- BFS : 모든 가중치가 1로 동일할 때 O(E)
  - collections의 deque를 사용함. 근데 순서가 필요한 경우엔 heapq를 사용한다
  - BFS는 큐에서 뺀 다음이 아닌, 큐에 넣을 때 방문 체크를 해야 중복 방문이 일어나지 않습니다. BFS 문제에서 시간 초과나 메모리 초과가 나면 이것부터 의심해 보시면 됩니다.
  - BFS를 할 때 큐의 크기가 제한되어 있도록 구현했다면, 그 크기는 적어도 방문할 수 있는 정점의 총 개수보다는 크게 합시다.

## 2. 최대값 (Backtracking)
### DFS vs BFS
- DFS : 절대로 최단거리를 구해 주지 않습니다. 물론 메모이제이션 없이 모든 경로를 탐색하는 DFS는 최단거리를 구해 주겠지만, 시간 초과가 날 것입니다.
- BFS : 트리 깊이가 무한대가 될 때. 미로찾기 루프 발생 시.



## Tips
1. [Runtime Error](http://www.secmem.org/blog/2020/09/19/rte/)
2. [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)