# start 21.04.14 AM09:00
# Reading 5mins
# Alg Writing  10mins

"""
left 0 down 1 right 2 up 3
torn move: (0, -1) (+1, 0) | (0, +2) (-2, 0) | (0, -3) (+3, 0) | (0, +4) (-4, 0) | ...  
sand move: calc mm & index in map
output: Init sum - Last sum
"""

# First Trial AM10:40 - 시간초과 (python3)
# Second Trial AM10:40 - (pypy3)
from math import floor


class Map:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pr = int(N/2)
        self.pc = int(N/2)
        self.mm = [
            [0, 0, 0.02, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0.05, 0, 0, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0, 0, 0.02, 0, 0]
            ]
        self.mms = []
        self.out_sand = 0
        self.init_sand = self.sum_sand()
        self.curr_sand = 0
        
        self.step = 0
        self.move_len = 1
        self.pd = 0
        self.dirs = [
            [0, -1], [+1, 0], [0, +1], [-1, 0]
        ]
        self.gen_mms()
        return
    
    def sum_sand(self):
        t = 0
        for r in range(self.N):
            for c in range(self.N):
                t += self.M[r][c]
        return t
    
    def printM(self):
        for r in range(self.N):
            for c in range(self.N):
                if self.pr == r and self.pc == c:
                    print(f"T/{self.M[r][c]}", end=' ')
                else:
                    print(f"0/{self.M[r][c]}", end=' ')
            print('\n')
        print("===================")
    
    def gen_mms(self):
        # left
        self.mms.append(self.mm)
        
        # down
        t = []
        for c in range(4, -1, -1):
            tmp = []
            for r in range(4, -1, -1):
                tmp.append(self.mm[r][c])
            t.append(tmp)
        self.mms.append(t)
        
        # right
        t = []
        for r in range(4, -1, -1):
            tmp = []
            for c in range(4, -1, -1):
                tmp.append(self.mm[r][c])
            t.append(tmp)
        self.mms.append(t)
        
        # up
        t = []
        for c in range(0, 5):
            tmp = []
            for r in range(0, 5):
                tmp.append(self.mm[r][c])
            t.append(tmp)
        self.mms.append(t)
        return
    
    def torn_move(self):
        dr, dc = self.dirs[self.pd]
        # dr, dc = dr * self.move_len, dc * self.move_len
        nr, nc = self.pr + dr, self.pc + dc
        self.pr, self.pc = nr, nc
        self.step += 1
        return
    
    def torn_dir_update(self):
        if self.step < self.move_len:
            pass
        elif self.step == self.move_len:
            self.pd += 1
            self.pd = self.pd % 4
            self.step = 0
            if self.pd % 2 == 0:
                # print(self.pd, '/', self.move_len)
                self.move_len += 1
        else:
            print(self.step)
            print(self.move_len)
            raise RuntimeError
        return
    
    def sand_move(self):
        out_sand = 0
        in_sand = 0
        nb_sand = self.M[self.pr][self.pc]
        self.M[self.pr][self.pc] = 0
        
        for i, r in enumerate(range(self.pr-2, self.pr+3)):
            for j, c in enumerate(range(self.pc-2, self.pc+3)):
                mm = self.mms[self.pd]
                perc = mm[i][j]
                sand_perc = floor(nb_sand * perc)
                if 0 <= r <= self.N-1 and 0 <= c <= self.N-1:
                    self.M[r][c] += sand_perc
                    in_sand += sand_perc
                else:
                    out_sand += sand_perc
        
        alpha = nb_sand - out_sand - in_sand
        # self.printM()
        
        ar, ac = self.pr + self.dirs[self.pd][0], self.pc + self.dirs[self.pd][1]
        if 0 <= ar <= self.N-1 and 0 <= ac <= self.N-1:
            self.M[ar][ac] += alpha
        else:
            out_sand += alpha
        
        self.out_sand += out_sand
        return
    
    def sand_calc(self):
        self.curr_sand = self.sum_sand()
        if (self.init_sand - self.curr_sand) != self.out_sand:
            print('out        : ', self.out_sand)
            print('init - curr: ', self.init_sand - self.curr_sand)
            raise RuntimeError
        else:
            return self.out_sand
    
    def run(self):
        while not(self.pr == 0 and self.pc == -1):
            self.torn_move()
            self.sand_move()
            self.torn_dir_update()
            # self.printM()
        
        ret = self.sand_calc()
        return ret

def main():
    N = list(map(int, input().split()))[0]
    tbl = []
    for _ in range(N):
        tbl.append(list(map(int, input().split())))
    m = Map(N, tbl)
    ret = m.run()
    print(ret)
    return

if __name__ == '__main__':
    main()
