# start 21.04.09 AM11:00
# Reading 5mins
# Alg Writing  10mins
# First AM12:30 - Runtime Error(Index Error)

drc = [
    [-1, -1, 0, 1, 1, 1, 0, -1], 
    [0, 1, 1, 1, 0, -1, -1, -1]
]
rN = 0

class Ball():
    def __init__(self, _id, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d
        self.id = _id
    
    def __str__(self):
        ret = f"\n{self.id}: ({self.r}/{self.c}) s {self.s} d {self.d} | m {self.m} "
        return ret
    
    @staticmethod
    def change(nrc):
        if 0 <= nrc <= rN:
            ret = nrc
        elif nrc < 0:
            ret = nrc + (rN + 1)
        elif rN < nrc:
            ret = nrc - (rN + 1)
        else:
            raise RuntimeError
        return ret
    
    def move(self):
        global rN
        dr, dc = self.s * drc[0][self.d], self.s * drc[1][self.d]
        nr, nc = self.r + dr, self.c + dc
        self.r, self.c = self.change(nr), self.change(nc)
        return

class Map():
    def __init__(self, _cnt, _list, _ids, _dirs, _ss, balls, k, N):
        self._cnt = _cnt
        self._list = _list
        self._id = _ids
        self._dir = _dirs
        self._ss = _ss
        self.balls = balls
        self.k = k
        self.N = N
        self.ball_id = len(balls)
        self.iter_cnt = 0
        # self.collapsed = []
        self.map_update()
        return
    
    def printM(self, mode):
        print(f"======{self.iter_cnt}========")
        if mode == 'id':
            print("=====ID/DIR/SP=====")
            for i in range(self.N):
                for j in range(self.N):
                    print(f"{self._id[i][j]}/{self._dir[i][j]}/{self._ss[i][j]}", end=' ')
                print('\n')
            print('\n')
            
        if mode == 'cnt':
            print("=====CNT=====")
            for i in range(self.N):
                for j in range(self.N):
                    print(self._cnt[i][j], end=' ')
                print('\n')
            print('\n')
        return
    
    def map_update(self):
        for i in range(self.N):
            for j in range(self.N):
                self._cnt[i][j] = 0
                self._list[i][j] = []
                self._id[i][j] = 0
                self._dir[i][j] = 0
                self._ss[i][j] = 0
        
        for k in self.balls:
            b = self.balls[k]
            r, c = b.r, b.c
            self._cnt[r][c] += 1
            self._list[r][c].append(k)
            self._id[r][c] = b.id
            self._dir[r][c] = b.d
            self._ss[r][c] = b.s
        
        # self.printM('cnt')
        # self.printM('id')
        return
    
    def ball_move(self):
        for k in self.balls:
            b = self.balls[k]
            b.move()
    
    def check_dir(self, old_d, d):
        # init -99
        # even 0
        # odd 1
        pre_d = d % 2
        if old_d == -99:
            return pre_d
        
        if old_d == pre_d:
            return pre_d
        else:
            return -1
    
    def ball_update(self, r, c):
        bls = self._list[r][c]
        m, s, old_d = 0, 0, -99
        for bb in bls:
            b = self.balls[bb]
            m += b.m
            s += b.s
            old_d = self.check_dir(old_d, b.d)
            b._id = -1
            del self.balls[bb]
        
        if old_d == 1 or old_d == 0:
            ds = [0,2,4,6]
        else:
            ds = [1,3,5,7]
        
        ms, ss = int(m/5), int(s/len(bls))
        for i in range(4):
            self.ball_id += 1
            b = Ball(self.ball_id, r, c, ms, ss, ds[i])
            self.balls[self.ball_id] = b
    
    def ball_remove(self):
        rmv = []
        ret = 0
        for k in self.balls:
            bs = self.balls[k]
            mm = bs.m
            ret += mm
            if mm == 0:
                rmv.append(k)
        
        for k in rmv:
            del self.balls[k]
        
        return ret
    
    def run(self):
        ret = 0
        for _ in range(self.k):
            self.ball_move()
            self.map_update()
            
            for i in range(self.N):
                for j in range(self.N):
                    if self._cnt[i][j] > 1:
                        self.ball_update(i, j)
            ret = self.ball_remove()
            # self.map_update()
            self.iter_cnt += 1
        return ret

def main():
    global rN
    N, M, k = list(map(int, input().split()))
    rN = N - 1
    
    bdict = {}
    for i in range(1, M+1):
        r, c, m, s, d = list(map(int, input().split()))
        b = Ball(i, r-1, c-1, m, s, d)
        bdict[i] = b
    
    # for kk in bdict:
    #     b = bdict[kk]
        # print(b)
    # print("")
    tbl_cnt = [[0 for _ in range(N)] for _ in range(N)]
    tbl_list = [[[] for _ in range(N)] for _ in range(N)]
    tbl_id = [[0 for _ in range(N)] for _ in range(N)]
    tbl_dir = [[0 for _ in range(N)] for _ in range(N)]
    tbl_ss = [[0 for _ in range(N)] for _ in range(N)]
    M = Map(tbl_cnt, tbl_list, tbl_id, tbl_dir, tbl_ss, bdict, k, N)
    ret = M.run()
    print(ret)


if __name__ == '__main__':
    main()

