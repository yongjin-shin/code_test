# DFS, backtracking
# 이슈: 일단 이동하고, 다시 돌려야하는데 이 때 deepcopy를 사용하자.
from heapq import heappop, heappush
from copy import deepcopy


dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, -1, -1, -1, 0, 1, 1, 1]
TOT = 16
Death = 0
alive = 0
fish = {}
MAX_SCORE = -99999


def printM(M, F):
    print(F)
    for i in range(4):
        for j in range(4):
            fid = M[i][j]
            if fid in F:
                print(f"{M[i][j]}/{F[fid][-1]}", end=' ')
            else:
                print(f"{M[i][j]}/-1", end=' ')
        print('\n')
    print('\n')
    return


def printF(F):
    for k in F:
        print(F[k])
    print('\n')
    return

    
def in_map(tx, ty):
    if 0 <= tx <= 3 and 0 <= ty <= 3: return True
    else: return False


def in_shark(M, tx, ty):
    if M[tx][ty] < 0:
        return True
    return False

def eatable(M, p):
    if M[p[0]][p[1]] > 0:return True
    return False

def swap(M, F, a, b):
    fid, fx, fy, new_dir = a
    tid, tx, ty = b
    M[fx][fy] = tid
    M[tx][ty] = fid
    F[fid][1], F[fid][2], F[fid][3] = tx, ty, new_dir
    
    if tid > 0:
        F[tid][1], F[tid][2] = fx, fy
    elif tid == 0:
        pass
    else:
        raise RuntimeError
        
    # printM(M, F)
    return M, F


def fish_move(M, F):
    for k in F:
        fid, fx, fy, fdir = F[k]
        
        for i in range(8):
            pdirx, pdiry = dxs[fdir], dys[fdir]
            if i == 0:
                tdir = fdir
                tdirx, tdiry = pdirx, pdiry
            else:
                tdir = fdir + i
                if tdir > 7:
                    tdir = tdir % 8
                tdirx, tdiry = dxs[tdir], dys[tdir]
            
            tx, ty = fx + tdirx, fy + tdiry
            if in_map(tx, ty):
                if not in_shark(M, tx, ty):
                    tid = M[tx][ty]
                    M, F = swap(M, F, (fid, fx, fy, tdir), (tid, tx, ty))
                    break

    #     print("\n")
    # printM(M, F)
    return M, F


def shark_eat(M, F, p):
    fid = M[p[0]][p[1]]
    fdir = F[fid][3]
    del F[fid]
    M[p[0]][p[1]] = -1
    # printM(M, F)
    # print(F)
    return fid, fdir, F


def DFS(state, M, F):
    global MAX_SCORE
    
    _score = state[0]
    px, py = state[1], state[2]
    _dir = state[3]
    dx, dy = dxs[_dir], dys[_dir]

    for i in range(1, 4):
        tx, ty = px + dx*i, py + dy*i
        if in_map(tx, ty):
            new_M = deepcopy(M)
            new_F = deepcopy(F)
            
            new_M[px][py] = 0
            if eatable(new_M, (tx, ty)):
                fid, tdir, new_F = shark_eat(new_M, new_F, (tx, ty))
                new_M, new_F = fish_move(new_M, new_F)
                MAX_SCORE = max(MAX_SCORE, _score + fid)
                DFS([_score + fid, tx, ty, tdir], new_M, new_F)

def main():
    global fish
    inputs = [list(map(int, input().split())) for _ in range(4)]
    M = []
    
    fish_heap = []
    for row in range(4):
        li = inputs[row]
        tmp = []
        for col in range(4):
            id = li.pop(0)
            dir = li.pop(0)
            tmp.append(id)
            heappush(fish_heap, [id, row, col, dir-1])
        M.append(tmp)
    
    for i in range(16):
        f = heappop(fish_heap)
        fish[i+1] = f
    
    fid, tdir, fish = shark_eat(M, fish, (0, 0))
    M, fish = fish_move(M, fish)
    DFS([fid, 0, 0, tdir], M, fish)
    print(MAX_SCORE)


if __name__ == '__main__':
    main()


