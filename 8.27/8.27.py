import sys

N, M, K = map(int, input().split(" "))
data = list(map(int, sys.stdin.readline().split()))
print(data)
def Big_num(data):
    data.sort()
    max = data[-1]
    max2 = data[-2]
    count1 = (M//(K+1)) #2
    count2 = M - (M//(K+1)) # 8 - 2 = 6
    return (max * count2) + (max2 * count1) #6 * 6 + 5 * 2 = 46

print(Big_num(data))
