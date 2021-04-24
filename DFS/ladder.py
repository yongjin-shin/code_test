# START 21.04.22 PM19:22
# READ&IDEA Total Case : 3,000,000
# FAIL PM21:00

"""
그냥 combination으로 풀려고, init에서 옆에 있는것들 제거하고
조합을 만들었는데, 생각해보니 이렇게 해버리면 연결된 부분들이 생겨버림...
결국 DFS로 처리해야함. 뭔가 순서를 만들면 편할 것 같았는데, 그냥 for loop 돌면서 해야할 듯;;
으아... 왜 이렇게 안되지ㅠㅠ

1) 일단 Combination은 모든 케이스들 다 체크하면 통과됨.
2) DFS는 그냥 exit을 해버리면 안됨...찾았다고 무조건 exit해버리면 가장 적은 수를 못 찾음!
"""

#! 풀이2

class Map():
    def __init__(self, N, H, infos):
        self.C = N
        self.R = H
        self.infos = infos
        self.visited = self.check()
        self.MIN = 4
    
    @staticmethod
    def printM(tbl):
        print('\n')
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print('='*10)
        return
    
    def check(self):
        visited = [[0 for _ in range(self.C)] for _ in range(self.R)]
        for info in self.infos:
            r, c = info
            visited[r-1][c-1] = 1
        return visited

    def sim(self, visited):
        for c in range(self.C):
            nc = c
            for r in range(self.R):
                if visited[r][nc]:
                    nc += 1
                else:
                    if nc > 0 and visited[r][nc-1]:
                        nc -= 1
            if nc != c:
                return False
        return True

    def feasible(self, r, c):
        if 0 < c < self.C-1:
            if not (self.visited[r][c-1] or self.visited[r][c+1]):
                return True
        
        if 0 == c:
            if not self.visited[r][c+1]:
                return True
        
        return False
    
    def DFS(self, rr, cc, round):
        if round >= self.MIN:
            return
        else:
            if self.sim(self.visited):
                if self.MIN >= round:
                    self.MIN = round
                return
        
        if round == 3:
            return
        else:
            for r in range(rr, self.R):
                ss = cc if rr == r else 0
                for c in range(ss, self.C-1):
                    if not self.visited[r][c] and self.feasible(r, c):
                        self.visited[r][c] = 1
                        self.DFS(r, c, round+1)
                        self.visited[r][c] = 0
    
    def run(self):
        self.DFS(0, 0, 0)
        if self.MIN == 4:
            return -1
        else:
            return self.MIN


def main():
    N, M, H = list(map(int, input().split()))
    infos = []
    for _ in range(M):
        infos.append(list(map(int, input().split())))
    m = Map(N, H, infos)
    ret = m.run()
    print(ret)


if __name__ == '__main__':
    main()



#! 풀이1
from itertools import combinations

class Map():
    def __init__(self, N, H, infos):
        self.R = H
        self.C = N
        self.infos = infos
        self.visited = self.check()
        self.totM = self.count()
    
    @staticmethod
    def printM(tbl):
        print('\n')
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print('='*10)
        return
    
    def check(self):
        visited = [[0 for _ in range(self.C)] for _ in range(self.R)]
        for info in self.infos:
            r, c = info
            visited[r-1][c-1] = 1
        return visited
    
    def count(self):
        ret = []
        for r in range(self.R):
            for c in range(self.C-1):
                if not self.visited[r][c]:
                    if c == 0:
                        if not self.visited[r][c+1]:
                            ret.append((r, c))
                    else:
                        if not self.visited[r][c-1] and not self.visited[r][c+1]:
                            ret.append((r, c))
        return ret
    
    def feasible(self, comb, N):
        V = [row[:] for row in self.visited]

        for i in range(N):
            r, c = comb[i]
            okay = True
            
            if c == 0:
                if self.visited[r][c] or self.visited[r][c+1]:
                    okay = False
            else:
                if self.visited[r][c] or self.visited[r][c+1] or self.visited[r][c-1]:
                    okay = False
            
            if not okay:
                return False, None
            else:
                V[r][c] = 1
        return True, V
    
    def recover(self, comb, N):
        for i in range(N):
            r, c = comb[i]
            self.visited[r][c] = 0
        return
    
    def sim(self, visited):
        for c in range(self.C):
            nc = c
            for r in range(self.R):
                if visited[r][nc]:
                    nc += 1
                else:
                    if nc > 0 and visited[r][nc-1]:
                        nc -= 1
            if nc != c:
                return False
        return True
    
    def run(self):
        if self.sim(self.visited):
            return 0
        
        for i in range(1, 4):
            combs = combinations(self.totM, i)
            for comb in combs:
                okay, V = self.feasible(comb, i)
                if okay:
                    if self.sim(V):
                        return i
        return -1

def main():
    N, M, H = list(map(int, input().split()))
    infos = []
    for _ in range(M):
        infos.append(list(map(int, input().split())))
    m = Map(N, H, infos)
    ret = m.run()
    print(ret)


if __name__ == '__main__':
    main()
