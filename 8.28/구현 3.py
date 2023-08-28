inputs = input()
# 입력한 문자를 체스판의 행과열로 변환한다.
rows = int(ord(inputs[0]) - ord('a')) + 1
columns = int(inputs[1])
count = 0

# 경우의 수를 나열한다.
steps = [(1, -2), (1, 2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

# 경우의 수 하나씩 대입해보면서
for step in steps:
    nrows = rows + step[0]
    ncolumns = columns + step[1]

    #조건에 부합한다면 count + 1 을 수행한다.
    if nrows >=1 and nrows <=8 and ncolumns >=1 and ncolumns <= 8:
        count += 1

print(count)