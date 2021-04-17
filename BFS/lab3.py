# START 21.04.17 PM 17:10
# READING & IDEA PM 17:40
# PAUSED PM 18:50

# First Trial PM 21:00 - Wrong 85%??
# Second Trial PM 21:45 

"""
문제를 정확하게 이해 못 했다.
복사하는데 1초 걸리는줄 알았는데... 활성화도 1초가 걸린다는 사실에..
더 어렵게 풀었네 ~_~
=========================================================
=========================================================

DFS (재귀)
- 어쨌거나 M개를 선택해야만 시간이 얼마나 걸리는지 알 수 있다
- 걱정거리: 50개 중에 10개 선택하는 경우의 수는 꽤 많은데 
          가 아니라 M<=10에서 선택되므로 가짓수는(300백만 ~ 0.03초)
=========================================================
굳이?? 그냥 Combination 다 구해서 하나씩 체크해도 충분할 듯. 재귀보단 더 간단하지 싶음. 어차피 동일한거

최단시간 (BFS)
- 체크 1) Step마다 감염영역 갯수 트래킹. 늘어나는 양이 0이 되면 점검.
      2) 만약 전체크기 != 감염영역 return -1
      3) 

특이사항
- 비활성에 닿으면 비활성도 활성으로 역할함
"""
import sys; input=sys.stdin.readline
from itertools import combinations # permutation
from collections import deque

MIN = 99999999

class Map():
    def __init__(self, N, K, tbl):
        self.N = N
        self.K = K
        self.M = tbl
        self.li_A = []
        self.MIN = 99999999
        self.nb_emp = self.count()
        self.dirs = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]
    
    def feasible(self, r, c):
        if (0 <= r < self.N and 0 <= c < self.N) and (self.M[r][c] != -1):
            return True
        else:
            return False
    
    def check_b(self, r, c):
        ret = True if self.M[r][c] == -2 else False
        return ret
    
    def count(self):
        nb_emp = 0
        for r in range(self.N):
            for c in range(self.N):
                if self.M[r][c] == 2:
                    self.li_A.append((r, c))
                elif self.M[r][c] == 0:
                    nb_emp += 1
                self.M[r][c] *= -1
        return nb_emp
        
    def perm(self):
        ret = combinations(self.li_A, self.K)
        return list(ret)
    
    @staticmethod
    def printM(M):
        print('\n')
        for row in M:
            for c in row:
                print(c, end=' ')
            print('\n')
        print("=================")
        return
    
    def sim(self, agents):
        tbl = [row[:] for row in self.M]
        init = []
        nb_empty = self.nb_emp
        for a in agents:
            r, c = a
            init.append((r, c))
            tbl[r][c] =  1
        
        tic = 0
        dq = deque(init)
        while True:
            flag = True
            if nb_empty == 0:
                break
            
            sub_dq = []
            while dq:
                r, c = dq.popleft()
                for d in self.dirs:
                    nr, nc = r + d[0], c + d[1]
                    if self.feasible(nr, nc) and tbl[nr][nc] <= 0:
                        if self.check_b(nr, nc):
                            if flag:
                                tic += 1
                                flag = False
                            
                            tbl[nr][nc] = 1
                            sub_dq.append((nr, nc))
                        else:
                            if flag:
                                tic += 1
                                flag = False
                                # print(tic)
                            
                            tbl[nr][nc] = tic
                            nb_empty -= 1
                            sub_dq.append((nr, nc))
            
            # self.printM(tbl)
            if len(sub_dq) > 0:
                dq = deque(sub_dq)
            else:
                break
        
        if nb_empty == 0:
            return tic
        else:
            return -1
    
    def run(self):
        # if self.nb_emp == 0:
        #     return 0
        
        perm = self.perm()
        for p in perm:
            t = self.sim(p)
            if 0 <= t <= self.MIN:
                self.MIN = t
            # break
            # print("")
        
        if self.MIN < MIN:
            return self.MIN
        else:
            return -1


def main():
    N, K = list(map(int, input().split()))
    tbl = []
    for _ in range(N):
        tbl.append(
            list(map(int, input().split()))
        )
    
    M = Map(N, K, tbl)
    ret = M.run()
    print(ret)

if __name__ == '__main__':
    main()
