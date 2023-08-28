n,m = map(int,input().split())
x,y,direction = map(int,input().split())

map_list = []
for i in range(n) :
    map_list.append(list(map(int,input().split())))

# 0 : 북, 1 : 동, 2: 남, 3 : 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
mark = [ [0] * m for _ in range(n)]
mark[x][y] = 1
turn_count = 0

while True :
    # 왼쪽으로 회전
    direction -= 1
    if direction < 0 :
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 칸이 있는 경우
    if map_list[nx][ny] == 0 and mark[nx][ny] ==0 :
        mark[nx][ny] = 1
        x += dx[direction]
        y += dy[direction]
        turn_count = 0
    # 해당 방향으로 다 가본 경우
    else :
        turn_count += 1

    if turn_count == 4 :
        # 뒤로 갈 수 있는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map_list[nx][ny] == 0 :
            x = nx
            y = ny
            turn_count = 0
        # 뒤로 갈 수 없는 경우
        else:
            break

count = 0
for i in range(n):
    count += mark[i].count(1)

print(count)
