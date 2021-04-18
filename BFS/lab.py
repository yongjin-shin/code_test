# START 21.04.18 PM14:44
# READING & IDEAS 
# Fist Trial 21.04.18 PM15:15 Done
"""
3개 선택하는 가짓수 <= 4만개
일단 모든 경우의 수로 다 체크해봐도 충분할 듯

안전 영역 ==> BFS
- deque에 다 쌓아두고, 끝날 때까지 진행하면 될 듯
- 문제가 되는 것은 무엇일까?

"""

from itertools import combinations
from collections import deque
import sys; input = sys.stdin.readline


MAX = -1

class Map():
    def __init__(self, N, M, tbl):
        self.R = N
        self.C = M
        self.M = tbl
        self.nb_empty, self.empty_set, self.agent_set= self.count()
        self.MAX = MAX
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    @staticmethod
    def printM(tbl):
        print('\n')
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print("="*10)
        return
    
    def count(self):
        nb_empty = 0
        empty_set = []
        agent_set = []
        for r in range(self.R):
            for c in range(self.C):
                if self.M[r][c] == 0:
                    nb_empty += 1
                    empty_set.append((r, c))
                elif self.M[r][c] == 2:
                    agent_set.append((r, c))
        
        nb_empty -= 3
        return nb_empty, empty_set, agent_set
    
    def feasible(self, r, c):
        if 0<=r<self.R and 0<=c<self.C:
            return True
        return False
        
    def BFS(self, brs):
        nb_empty = self.nb_empty
        m = [row[:] for row in self.M]
        for b in brs:
            r, c = b
            m[r][c] = 1
        # self.printM(m)
        
        dq = deque(self.agent_set)
        while dq:
            r, c = dq.popleft()
            for d in self.dirs:
                nr, nc = r + d[0], c + d[1]
                if self.feasible(nr, nc):
                    if m[nr][nc] == 0:
                        dq.append((nr, nc))
                        m[nr][nc] = 2
                        nb_empty -= 1
        # self.printM(m)
        return nb_empty
        
    def run(self):
        pp = combinations(self.empty_set, 3)
        for p in pp:
            t = self.BFS(p)
            if self.MAX <= t:
                self.MAX = t
        
        return self.MAX


def main():
    N, M = list(map(int, input().split()))
    tbl = []
    for _ in range(N):
        tbl.append(list(map(int, input().split())))
    m = Map(N, M, tbl)
    ret = m.run()
    print(ret)


if __name__ == '__main__':
    main()
