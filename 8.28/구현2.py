n = int(input())

count = 0
if n >= 23:
    count = (3600*3) + (n-2) * 1575
elif n >=13:
    count = (3600*2) + (n-1) * 1575
elif n >=3:
    count = (3600) + (n) * 1575
else:
    count = (n+1) * 1575

print(count)

