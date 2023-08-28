n = int(input())


cmds = list(map(str, input().split()))

def maps(cmds, n):
    x, y = 1, 1
    LR = ["L", "R"]
    UD = ["U", "D"]
    for z in cmds:
        if z in LR:
            if z=="L":
                if y <=1:
                    continue
                y-= 1
            else:
                if y >=n:
                    continue
                y += 1
        elif z in UD:
            if z == "U":
                if x <=1:
                    continue
                x-= 1
            else:
                if x >=n:
                    continue
                x += 1
        else:
            continue

    return x, y
x, y = maps(cmds, n)
print(x, y)