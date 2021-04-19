# START 21.04.19 PM 19:30
# READ & IDEA
# First Trial 21.04. 19 PM20:43
"""
처음에 뭔가 했는데, 그냥 BFS로 하나씩 처리하면 되었다.
고민했던 부분은, Window를 만들어두고 이동시킬까 했는데, numpy가 아니라서 더 오래걸릴 것 같았다.
그래서 그냥 map 복사해서 체크해나가는 것으로 바꿨음.
언제까지 찾아야 하나 고민을 했는데, 중앙에서 지역 전체를 모두 cover하는 케이스가 worst case라고 생각했음
모두 다 집인 케이스에는 그냥 return nb_hs로 하긴 했는데, 이거 좀 야매인듯;;;
"""
from collections import deque


class Map():
    def __init__(self, N, M, tbl):
        self.N = N
        self.K = M
        self.M = tbl
        self.E = [[0 for _ in range(N)] for _ in range(N)]
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.hs, self.nb_hs = self.count()
        self.maxw = self.max_w()
        self.MAX = -1
        self.MAX_house = -1
        # self.printM(tbl)
        # print("")
    
    @staticmethod
    def printM(tbl):
        print('\n')
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print('='*10)
        return
    
    def feasible(self, r, c):
        if 0<=r<self.N and 0<=c<self.N:
            return True
        return False
    
    def max_w(self):
        m = int(self.N / 2)
        visited = [row[:] for row in self.E]
        lv = 0
        
        dq = deque([(m, m)])
        visited[m][m] = 1
        cnt = 1
        cover = False
        
        while not cover:
            sub_dq = []
            lv += 1
            while dq:
                r, c = dq.popleft()
                for d in self.dirs:
                    nr, nc = r + d[0], c + d[1]
                    if self.feasible(nr, nc) and not visited[nr][nc]:
                        sub_dq.append((nr, nc))
                        visited[nr][nc] = 1
                        cnt += 1
            # self.printM(visited)
            # self.printM(self.M)
            dq = deque(sub_dq)
            if cnt == self.N*self.N:
                cover = True
        return lv
            
    
    @staticmethod
    def cost(level):
        ret = level * level + (level - 1) * (level - 1)
        return ret
    
    def count(self):
        hs = []
        cnt = 0
        for r in range(self.N):
            for c in range(self.N):
                if self.M[r][c] == 1:
                    hs.append((r, c))
                    cnt += 1

        return hs, cnt
        
    def sim(self, r, c):
        visited = [row[:] for row in self.E]
        visited[r][c] = 1
        
        lv = 1
        cnt = 0
        if self.M[r][c] == 1:
            cnt += 1
            visited[r][c] = 2

        profit = cnt * self.K - self.cost(lv)
        if profit >= 0 and self.MAX_house <= cnt:
            self.MAX_house = cnt
        
        # self.printM(visited)
        # print(f"{self.MAX}|{self.MAX_house} vs {profit}|{cnt}")
        
        dq = deque([(r, c)])
        for _ in range(self.maxw):
            sub_dq = []
            lv += 1
            while dq:
                r, c = dq.popleft()
                for d in self.dirs:
                    nr, nc = r + d[0], c + d[1]
                    if self.feasible(nr, nc) and not visited[nr][nc]:
                        sub_dq.append((nr, nc))
                        visited[nr][nc] = 1
                        if self.M[nr][nc]:
                            cnt += 1
                            visited[nr][nc] = 2
            
            profit = cnt * self.K - self.cost(lv)
            if profit >= 0 and self.MAX_house <= cnt:
                self.MAX_house = cnt
            
            # self.printM(visited)
            # print(f"{self.MAX}|{self.MAX_house} vs {profit}|{cnt}")
            dq = deque(sub_dq)
        return
        
    def run(self):
        if self.nb_hs == self.N * self.N:
            return self.nb_hs
        
        for r in range(self.N):
            for c in range(self.N):
                # if r == 3 and c == 3:
                    # print("")
                self.sim(r, c)
        return self.MAX_house


def main():
    T = int(input())
    for test_case in range(1, T + 1):
        N, M = list(map(int, input().split()))
        tbl = []
        for _ in range(N):
            tbl.append(
                list(map(int, input().split()))
            )
        m = Map(N, M, tbl)
        ret = m.run()
        print(f"#{test_case} {ret}")


if __name__ == '__main__':
    main()
