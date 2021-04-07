def f1(a, b):
    ret = 2/(1/a + 1/b)
    print(ret)
    
f1(0.00687, 0.98)
f1(0.09, 0.95)

# # import sys
# # sys.stdin.readline().rstrip()

# # n = int(input())
# # data = map(int, input().split())
# # data = list(data)

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]


# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#     return


# f = open('test.txt', 'r')
# nv, ne = list(map(int, f.readline().rsplit()))
# parent = [i for i in range(nv+1)]

# edges = []
# result = 0

# for _ in range(ne):
#     a, b, cost = list(map(int, f.readline().rsplit()))
#     edges.append((cost, a, b))

# edges.sort()
# for eg in edges:
#     cost, a, b = eg
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         print(result)

# print(parent)
# print(result)

