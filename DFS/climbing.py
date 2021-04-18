# START 21.04.18 PM 17:00
# READ & IDEA
# First Trial PM18:22
"""
BFS
못 가면, 한번 팔 수 있다. 
- Feasibility 체크할 때 조심할 것.
- 모든 방향으로 갈 수가 있음.

BFS보다 DFS를 해야할 삘인데??? PM18:00

"""

# import sys; input = sys.stdin.readline
from collections import deque


MAX = -1

class Map():
    def __init__(self, N, K, tbl):
        self.N = N
        self.K = K
        self.m = tbl
        self.visited = [[0 for _ in range(N)] for _ in range(N)]
        self.hills = self.count()
        self.MAX = MAX
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        return
    
    def reset(self, N, K, tbl):
        self.N = N
        self.K = K
        self.m = tbl
        self.MAX = MAX
        self.hills = self.count()
        return
    
    def count(self):
        _max = -1
        max_pos = []
        for row in self.m:
            for c in row:
                if _max <= c:
                    _max = c
        
        for r in range(self.N):
            for c in range(self.N):
                if self.m[r][c] == _max:
                    max_pos.append((r, c))
        return max_pos
    
    def exists(self, r, c):
        if 0<=r<self.N and 0<=c<self.N:
            return True
        return False
    
    @staticmethod
    def moveable(pv, nv):
        if pv - nv > 0:
            return True
        return False
        
    def DFS(self, r, c, step, chance, pv, visited):
        V = [row[:] for row in visited]
        V[r][c] = 1
        # print(r, c, step, chance, pv)
        
        for d in self.dirs:
            nr, nc = r + d[0], c + d[1]
            if self.exists(nr, nc) and not V[nr][nc]:
                # pv = self.m[r][c]
                nv = self.m[nr][nc]
                nstep = step + 1
                nchance = chance
                if self.moveable(pv, nv):
                    self.DFS(nr, nc, nstep, nchance, nv, V)
                
                if chance:
                    for k in range(1, self.K+1):
                        nnv = nv - k
                        if nnv < 0:
                            break
                        
                        if self.moveable(pv, nnv):
                            nchance = False
                            self.DFS(nr, nc, nstep, nchance, nnv, V)
        
        if step >= self.MAX:
            self.MAX = step
        return
        
    def run(self):
        for hill in self.hills:
            r, c = hill
            self.DFS(r, c, 1, True, self.m[r][c], self.visited)
        return self.MAX

def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N, K = list(map(int, input().split()))
        tbl = []
        for _ in range(N):
            tbl.append(list(map(int, input().split())))
        m = Map(N, K, tbl)
        ret = m.run()
        print(f"#{test_case} {ret}")


if __name__ == '__main__':
    main()
