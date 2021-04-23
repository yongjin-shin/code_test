# START 21.04.23 PM 16:05
# READ&IDEA
"""
DFS: MAX로 관리하면 됨
Simulation을 만드는게 이슈일 듯
Simulation 쪽 잘 못 연결해서 30분 날려먹은 듯..

그리고, route를 좀 더 쉽게 만들었으면, 
sim 함수에서 for loop를 없애서 시간을 줄 일 수 있을 듯

"""
# END 21.04.23 PM 18:15

from collections import deque

class Map():
    def __init__(self, _order):
        self.idx, self.nxt, self.scr, self.info = self.make()
        self._order = _order
        self.MAX = -1
        self.dices = [0, 0, 0, 0]
    
    def make(self):
        idx = [i for i in range(33)]
        nxt = [i for i in range(1, 33)] + [-1]
        scr = [0, 
               2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 
               13, 16, 19, 
               22, 24, 
               28, 27, 26, 
               25, 
               30, 35, 
               0]
        nxt[20], nxt[23], nxt[25], nxt[29], nxt[31] = 32, 29, 29, 30, 20
        info = {5: 21, 10: 24, 15: 26}
        return idx, nxt, scr, info
    
    def sim(self, pos, n):
        if pos in self.info.keys():
            pos = self.info[pos]
        else:
            if -1 == pos:
                return pos
            else:
                pos = self.nxt[pos]
        
        for i in range(1, n):
            if pos == -1:
                return pos
            else:
                pos = self.nxt[pos]
        return pos
    
    def get_score(self, score):
        s = 0
        for row in score:
            for c in row:
                s += self.scr[c]
        return s
    
    def DFS(self, dq, dices, score):
        if len(dq) == 0:
            # tt = self.get_score(score)
            if score >= self.MAX:
                self.MAX = score
                # print(dices, score, self.MAX)
            return
        
        n = dq.popleft()
        for i in range(4):
            if dices[i] == -1:
                continue 
            
            np = self.sim(dices[i], n)
            if np in dices:
                if np != -1:
                    continue
            
            # S = [row[:] for row in score]
            # S[i].append(np)
            S = score + self.scr[np]
            DICE = dices[:]
            DICE[i] = np
            DQ = deque(list(dq))
            self.DFS(DQ, DICE, S)
            
    
    def run(self):
        # self.DFS(deque(self._order), self.dices, [[], [], [], []])
        self.DFS(deque(self._order), self.dices, 0)
        return self.MAX
        print("")

def main():
    _order = list(map(int, input().split()))
    m = Map(_order)
    ret = m.run()
    print(ret)
    

if __name__ == '__main__':
    main()
