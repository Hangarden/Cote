import sys

N,M = map(int, input().split())
data = []

for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

print(data)

result = []
for x in data:
    x = min(x)
    result.append(x)

print(max(result))


#
# n, m = map(int, input().split())
# result = 0
#
# for _ in range(n):
#     data = list(map(int, input().split()))
#     x = min(data)
#     result = max(result, x)

print(result)
