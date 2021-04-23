# START 21.04.22 PM19:22
# READ&IDEA Total Case : 3,000,000
# FAIL PM21:00
"""
그냥 combination으로 풀려고, init에서 옆에 있는것들 제거하고
조합을 만들었는데, 생각해보니 이렇게 해버리면 연결된 부분들이 생겨버림...

결국 DFS로 처리해야함. 뭔가 순서를 만들면 편할 것 같았는데, 그냥 for loop 돌면서 해야할 듯;;
"""

class Map():
    def __init__(self, N, M, H, infos):
        self.N = N
        self.H = H
        self.M = M
        self.infos = infos
        self.visited = [[0 for _ in range(N)] for _ in range(H)]
        
        self.check()
        self.count()
    
    @staticmethod
    def printM(tbl):
        print('\n')
        for row in tbl:
            for c in row:
                print(c, end=' ')
            print('\n')
        print('='*10)
        return
    
    def count(self):
        checked = [[0 for _ in range(self.N)] for _ in range(self.H)]
        
        for r in range(self.H):
            for c in range(self.N):
                if self.visited[r][c]:
                    checked[r][c] = -1
                
                if 0 <= c < self.N-1:
                    if self.visited[r][c+1]:
                        checked[r][c] = -1
                    
        return checked
    
    def check(self):
        for info in self.infos:
            r, c = info
            r -= 1
            self.visited[r][c-1] = c
            self.visited[r][c] = c
        return
    
    def sim(self, visited):
        nr, nc = 0, 0
        for c in range(self.N-1):
            nc = c
            for r in range(self.H):
                nr = r
                # print(nc)
                if visited[nr][nc] > 0:
                    if 0 < nc < self.N-1:
                        if visited[nr][nc+1] == visited[nr][nc]:
                            nc += 1
                            continue
                        if visited[nr][nc-1] == visited[nr][nc]:
                            nc -= 1
                            continue
                    
                    elif 0 == nc:
                        if visited[nr][nc+1] == visited[nr][nc]:
                            nc += 1
                            continue
                    
                    elif nc == self.N-1:
                        if visited[nr][nc-1] == visited[nr][nc]:
                            nc -= 1
                            continue
                
            if nc != c:
                return False
        
        return True


    def feasible(self, r, c, C, V):
        if not V[r][c]:
            if 0 <= c < self.N-1:
                if not V[r][c+1]:
                    return True
        return False
    
    def DFS(self, visited, checked, round):
        if round == 3: 
            if self.sim(visited):
                return round
            else:
                return -1
        
        elif round < 3:
            if self.sim(visited):
                return round
            else:
                C = [row[:] for row in checked]
                for r in range(self.H):
                    for c in range(self.N-1):
                        if C[r][c] != -1 and self.feasible(r, c, C, visited):
                            V = [row[:] for row in visited]
                            self.printM(V)
                            self.printM(C)
                            V[r][c] = c+1
                            V[r][c+1] = c+1
                            C[r][c] = -1
                            self.printM(V)
                            self.printM(C)
                            ret = self.DFS(V, C, round+1)
                            if ret > 0:
                                return ret
                return -1
    
    def run(self):
        checked = self.count()
        ret = self.DFS(self.visited, checked, 0)
        return ret


def main():
    N, M, H = list(map(int, input().split()))
    infos = []
    for _ in range(M):
        infos.append(list(map(int, input().split())))
    m = Map(N, M, H, infos)
    ret = m.run()
    print(ret)


if __name__ == '__main__':
    main()

