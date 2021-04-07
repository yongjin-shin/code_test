
#! 시간 좀 더 빠르면 좋겠으나, 사실 2초 안에 충분히 들어가므로... 일단 정석대로, 깔끔하게 풀자!
#! 물고기 개수가 9개일 때, 체크하는거 대충하고 넘어갔는데 거기서 시간초과
#  7
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 1
#  1 1 1 1 1 1 9

# pass_or_eat
# find_minimal_path
# update_map
from collections import deque
from copy import deepcopy

M = []
V = []
N = 0
move = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}  ## 0-up 1-left 2-down 3-right
info = {'p': [-1, -1], 'n': 2, 'c': 0}


def find_baby():
    for i in range(N):
        for j in range(N):
            if M[i][j] == 9:
                state = (i, j)
                return state
    raise RuntimeError


def feasible(step):
    if step[0] < 0 or step[1] < 0: return False
    if step[0] == N or step[1] == N : return False
    if M[step[0]][step[1]] > info['n']: return False
    return True


def eatable(step):
    fish = M[step[0]][step[1]]
    if fish and fish < info['n'] and fish != 9: return True
    return False


def tup_add(a, b):
    c = [-1, -1]
    c[0] = a[0] + b[0]
    c[1] = a[1] + b[1]
    return c

def find_path():
    target = [-1, -1]
    min_dist = 9999999
    
    visited = deepcopy(V)
    next_moves = deque([info['p']])
    distance = deque([0])
    
    while next_moves:
        _now, dist = next_moves.popleft(), distance.popleft()
        # print(_now, dist)
        visited[_now[0]][_now[1]] = True
        if eatable(_now):
            if min_dist > dist:
                target[0], target[1] = _now[0], _now[1]
                min_dist = dist
            elif min_dist == dist:
                if target[0] > _now[0]:
                    target[0] = _now[0]
                    target[1] = _now[1]
                
                if target[0] == _now[0]:
                    if target[1] > _now[1]:
                        target[0] = _now[0]
                        target[1] = _now[1]
            else:
                pass
        
        for dir in move:
            _next = tup_add(_now, move[dir])
            # print(_next)
            if feasible(_next):
                if not visited[_next[0]][_next[1]]:
                    next_moves.append(_next)
                    distance.append(dist + 1)
                    visited[_next[0]][_next[1]] = True
    
    return target, min_dist


def update_map(_now, _next):
    M[_now[0]][_now[1]] = 0
    M[_next[0]][_next[1]] = 9
    return


def main():
    _next = [1, 1]
    tot_dist = 0
    while True:
        _now = [info['p'][0], info['p'][1]]
        _next, _dist = find_path()
        if _next[0] < 0 and _dist == 9999999:
            print(tot_dist)
            break
        else:
            tot_dist += _dist
        
        info['p'] = [_next[0], _next[1]]
        info['c'] += 1
        update_map(_now, _next)
        
        if info['c'] == info['n']:
            info['c'] = 0
            info['n'] += 1
        
        # print(_next, _dist)
        # print(info)
        # for i in range(N):
        #     for j in range(N):
        #         print(f"{M[i][j]}", end=' ')
        #     print('\n')
        # print('\n')



if __name__ == '__main__':
    # N = 4
    # M = [
    #     [4, 3, 2, 1],
    #     [0, 0, 0, 0],
    #     [0, 0, 9, 0], 
    #     [1, 2, 3, 4]
    #     ]
    
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    
    V = deepcopy(M)
    for i in range(N):
        for j in range(N):
            V[i][j] = False
    
    info['p'] = find_baby()
    main()

#============================
# https://www.acmicpc.net/source/27681823
# #원래는 bfs 쓸때 deque을 쓰는데 물고기 우선순위 때문에 heapq을 사
#============================

# from heapq import heappop, heappush


# dx=[0,-1,1,0]
# dy=[-1,0,0,1]

# n=int(input())
# pool=[list(map(int,input().split())) for x in range(n)]
# q=[]

# for y in range(n):
#     for x in range(n):
#         if pool[y][x] ==9:
#             heappush(q,(0,y,x))
#             pool[y][x]=0

# size=2
# cnt=0
# ans=0
# visit=[[0 for x in range(n)] for y in range(n)]

# while q:
#     d, y, x = heappop(q)
#     if 0< pool[y][x] < size:
#         cnt+=1
#         pool[y][x]=0
#         if cnt==size:
#             size+=1
#             cnt=0
#         ans+=d
#         d=0
#         q=[]
#         #물고기를 먹어서 visit배열 초기화
#         visit=[[0 for x in range(n)] for y in range(n)]

#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<n and 0<=ny<n and visit[ny][nx]==0 and pool[ny][nx] <= size:
#             visit[ny][nx]=1
#             heappush(q,(d+1,ny,nx))
            
# print(ans)
