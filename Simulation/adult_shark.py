# Simple Simulation
from heapq import heappush, heappop

# row, col
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Shark():
    def __init__(self, id, row, col, _dir, k):
        self.priority = None
        self.id = id
        self.row = row
        self.col = col
        self._dir = _dir
        self.k = k
    
    def set_dir(self, dir):
        self.dir = dir
    
    def set_priority(self, priority):
        self.priority = priority
        return
    
    def get_dir(self, _dir):
        return self.priority[_dir]
    
    def get_pos(self):
        return self.row, self.col
    
    def __str__(self):
        return f"id: {self.id}\npos: ({self.row}, {self.col})\ndir: {self._dir}\n"
    
    def feasible(self, M):
        no_sm = {}
        my_sm = {}
        # print(M)
        for i, dxy in enumerate(dirs):
            tx, ty = self.row + dxy[0], self.col + dxy[1]
            if not (0 <= tx <= M.N-1 and 0 <= ty <= M.N-1):
                continue
            
            if M.tbl[tx][ty][2]:
                if M.tbl[tx][ty][1] == self.id:
                    my_sm[i] = (tx, ty)
            else:
                no_sm[i] = (tx, ty)
                
        if len(no_sm) > 0:
            return no_sm
        else:
            return my_sm
    
    def move(self, M):
        targets = self.feasible(M)
        priors = self.get_dir(self._dir)
        for p in priors:
            if p in targets:
                M.tbl[self.row][self.col][0] = 0
                tmp = targets[p]
                self.row, self.col = tmp[0], tmp[1]
                self._dir = p
                # print(self)
                return
        
        M.printM()
        raise RuntimeError("Cannot Move")
        
class Map():
    def __init__(self, tbl, N, sharks, k):
        self.tbl = tbl
        self.sharks = sharks
        self.k = k
        self.time = 0
        self.N = N
    
    def game_end(self):
        if len(self.sharks) == 1 and self.sharks[0].id == 1:
            return True
        return False
        
    def time_out(self):
        if self.time > 1000:
            return True
        return False
    
    def move(self):
        for s in self.sharks:
            # print(s)
            s.move(self)
        return
    
    def __str__(self):
        print(f"======{self.time}========")
        ret = ""
        for i in range(self.N):
            for j in range(self.N):
                ret += f"{self.tbl[i][j]} "
            ret += "\n"
        ret += "\n"
        return ret
    
    def printM(self):
        # print(f"======{self.time}========")
        # for i in range(self.N):
        #     for j in range(self.N):
        #         print(self.tbl[i][j], end=' ')
        #     print('\n')
        # print('\n')
        # return
        pass
    
    def update(self):
        self.time += 1
        for i in range(self.N):
            for j in range(self.N):
                if not self.tbl[i][j][0] and self.tbl[i][j][2] > 1:
                    self.tbl[i][j][0] = 0  # visited = false
                    self.tbl[i][j][2] -= 1  # smell discount
                elif self.tbl[i][j][2] == 1:
                    self.tbl[i][j][0] = 0  # visited = false
                    self.tbl[i][j][1] = 0  # shark id
                    self.tbl[i][j][2] = 0  # shark sml
                else:
                    if self.tbl[i][j][0]:
                        raise RuntimeError("update wrong")
        # self.printM()
        
        for s in self.sharks:
            if self.tbl[s.row][s.col][0] == 0:
                self.tbl[s.row][s.col] = [1, s.id, self.k]
            else:
                if self.tbl[s.row][s.col][1] > s.id:
                    self.tbl[s.row][s.col] = [1, s.id, self.k]
                else:
                    s.id = -1
        
        tmp = []
        for i in range(len(self.sharks)):
            if self.sharks[i].id > 0:
                tmp.append(self.sharks[i])
        self.sharks = tmp
        self.printM()
        return
        
    def run(self):
        while True:
            if self.time_out():
                return -1
            else:
                if self.game_end():
                    return self.time
                self.move()
                self.update()


def main():
    N, M, k = list(map(int, input().split()))
    tbl = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    ss = []
    for row in range(N):
        tmp = list(map(int, input().split()))
        for col in range(N):
            if tmp[col] > 0:
                tbl[row][col][0] = 1
                tbl[row][col][1] = tmp[col]
                tbl[row][col][2] = k
                heappush(ss, [tmp[col], row, col])
    
    init_dir = list(map(int, input().split()))
    _dirs = dict(zip([i for i in range(M)], init_dir))
    sharks = []
    for i in range(M):
        s = heappop(ss)
        s = Shark(s[0], s[1], s[2], _dirs[i]-1, k)
        sharks.append(s)
        priority = {}
        for i in range(4):
            rl = list(map(int, input().split()))
            rl = [r-1 for r in rl]
            priority[i] = rl
        s.set_priority(priority)
    
    M = Map(tbl, N, sharks, k)
    ret = M.run()
    print(ret)
    
    
if __name__ == '__main__':
    main()
