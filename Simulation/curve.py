# START 21.04.20 PM19:30
# READ & IDEA PM19:40
# cheating PM21:00

# RESTART 21.04.22 PM18:50
# End 21.04.22 PM19:10

"""
1) 세대 증가
- 격자 중에 MAX, MIN 확인할 것
- 일단 모든 선분들 "하나씩" 뽑아서 90도 이동시키고,
- 마지막 점에서 더하기만 해주면 됨
이건 deque에서 하나씩 뽑아가면서 처리해주면 될 듯

2) 격자 둘러쌓인거 확인
- 세대 완성해서 visited 체크하고
- 2x2 window 만들어서 한점씩 체크해야할 듯
====================================================
아... 쉬운 문제였구나...
그냥 선분이라고 생각 안 하고, [이동한다]고 했으면 쉽게 푸는거구나...
괜히 회전 변화하고 그렇게 생각했네..

"""
from collections import deque


class Map():
    def __init__(self, infos):
        self.MAXR = 0
        self.MAXC = 0
        self.MINR = 102
        self.MINC = 102
        
        self.dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        self.infos = infos
        self.N = 101
        self.visited = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.cvs = self.generate()
    
    def feasible(self, r, c):
        if 0<=r<self.N and 0<=c<self.N:
            return True
        return False
    
    @staticmethod
    def printM(tbl):
        print("\n")
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print('='*10)
    
    def get_range(self, r, c):
        if self.MINR >= r:
            self.MINR = r
        
        if self.MINC >= c:
            self.MINC = c
            
        if self.MAXR <= r:
            self.MAXR = r
        
        if self.MAXC <= c:
            self.MAXC = c
    
    def make_curve(self, r, c, d, g, V):
        dd = self.dirs[d]
        nr, nc = r + dd[0], c + dd[1]
        self.visited[r][c] = V
        self.visited[nr][nc] = V
        self.get_range(r, c)
        self.get_range(nr, nc)
        
        if g == 0:
            return
        # self.printM(self.visited)
        dq =[d]
        for _ in range(1, g+1):
            add_dq = []
            for dd in dq[::-1]:
                nd = (dd + 1)%4
                add_dq.append(nd)
                _dir = self.dirs[nd]
                nnr, nnc = nr + _dir[0], nc + _dir[1]
                
                if self.feasible(nnr, nnc):
                    self.visited[nnr][nnc] = V
                    self.get_range(nnr, nnc)
                nr, nc = nnr, nnc
            dq += add_dq
            
            # self.printM(self.visited)
        return dq
    
    def generate(self):
        cvs = []
        for V, info in enumerate(self.infos):
            c, r, d, g = info
            cv = self.make_curve(r, c, d, g, V+1)
            cvs.append(cv)
        return cvs
    
    def check(self):
        cnt = 0
        for r in range(self.MINR, self.MAXR):
            for c in range(self.MINC, self.MAXC):
                if self.visited[r][c] and\
                    self.visited[r+1][c] and\
                        self.visited[r][c+1] and\
                            self.visited[r+1][c+1]:
                                cnt += 1
        return cnt
    
    def run(self):
        # self.printM(self.visited)
        ret = self.check()
        return ret
    

def main():
    N = int(input())
    infos = []
    for _ in range(N):
        infos.append(list(map(int, input().split())))
    m = Map(infos)
    ret = m.run()
    print(ret)

if __name__ == '__main__':
    main()
