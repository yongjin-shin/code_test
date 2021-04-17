"""
BFS
1st group
    check visited
    add group
2nd+ group
    group -> check visited initial
    check visited
    add group

if len(group) > 0:
    Calc
    

처음부터 말렸다. DFS BFS 중에 고민했고, BFS가 더 효율적으로 제거할 수 있을거라 생각했다.
근데, 생각보다 모든 Cell을 Search하는게 시간을 많이 잡아먹었다.
비효율적으로 Search 할 수 밖에 없다고 생각은 했는데,
바꾼 영역만을 다시 Search하는게 더 좋다는 것은 영역이 커질수록 영향을 많이 준다는 것을 깨달았다...
생각해보면 N=50일 때, 가장 마지막 일부 영역만 숫자가 바뀐다면,
굳이 처음부터 Search를 할 필요는 없을테니....아쉽다.
"""
# start 21.04.15 AM09:32
# Reading 3mins
# Alg Writing  7mins
# First AM10:42 - Wrong Answer
# Second 21.04.17 PM03:40 - Time
# Third 21.04.17 PM05:00 - PASS

import sys; input = sys.stdin.readline
from collections import deque


class MAP():
    def __init__(self, tbl, N, L, R):
        self.N = N
        self.L = L
        self.R = R
        self.M = tbl
        self.visited = None
        self.groups = None
        self.sums = None
        self.GM = None
        self.flag = True
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        self.raw_gm = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        self.raw_vis = [[0 for _ in range(self.N)] for _ in range(self.N)]
        # self.print(self.M)
        # print("")
    
    def print(self, tbl):
        print('\n')
        for i in range(self.N):
            for j in range(self.N):
                print(tbl[i][j], end=' ')
            print('\n')
        print("===================")
        return
    
    def feasible(self, r, c):
        if 0 <= r < self.N and 0 <= c < self.N:
            return True
        else:
            return False
    
    def thres(self, v):
        if self.L <= abs(v) <= self.R:
            return True
        else:
            return False
    
    def BFS(self, pr, pc, g):
        if not self.visited[pr][pc]:
            self.visited[pr][pc] = 1
            visited = [row[:] for row in self.visited]
            
            dq = deque([(pr, pc)])
            tmp = [(pr, pc)]
            _s = 0
            while dq:
                r, c = dq.popleft()
                visited[r][c] = 1
                self.GM[r][c] = g
                pv = self.M[r][c]
                _s += pv
                # print(dq)

                for d in self.dirs:
                    nr, nc = r+d[0], c+d[1]
                    if self.feasible(nr, nc) and not visited[nr][nc]:
                        nv = self.M[nr][nc]
                        if self.thres(nv - pv) and self.GM[nr][nc] < 0:
                            visited[nr][nc] = 1
                            self.visited[nr][nc] = 1
                            dq.append((nr, nc))
                            tmp.append((nr, nc))
                            # print(dq)
                            # self.visited[nr][nc] = 1
                            # tmp.append((nr, nc))
                            # _s += nv
                            # self.GM[nr][nc] = g
            if len(tmp) > 1:
                self.groups.append(tmp)
                self.sums.append(_s)
                return True
            else:
                self.GM[pr][pc] = 1
                return False
        else:
            return False
    
    def init_map(self):
        self.GM = [raw[:] for raw in self.raw_gm]
        self.visited = [raw[:] for raw in self.raw_vis]
        self.groups = []
        self.sums = []
        return
    
    def run(self):
        step = 0
        search = deque([])  #! 이게 진짜 좋은 부분인 듯.
        for i in range(self.N):
            for j in range(self.N):
                search.append((i, j))
        
        while self.flag:
            g = 2
            self.init_map()
            while search:
                i, j = search.popleft()
                if self.BFS(i, j, g):
                    g = g+1
            
            # self.print(self.GM)
            # self.print(self.visited)
            
            if len(self.groups):
                self.flag = True
                
                for gg, ss in zip(self.groups, self.sums):
                    avg_sums = ss//len(gg)
                    for cell in gg:
                        r, c = cell
                        self.M[r][c] = avg_sums
                        search.append((r,c))  #! 이게 진짜 좋은 부분인 듯.
                
                step += 1
                # self.print(self.M)
                # print("")
            else: 
                self.flag = False
            
        return step


def main():
    N, L, R = list(map(int, input().split()))
    tbl = []
    for _ in range(N):
        tbl.append(list(map(int, input().split())))
    m = MAP(tbl, N, L, R)
    ret = m.run()
    print(ret)

if __name__ == '__main__':
    main()
