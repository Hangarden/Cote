# N,M의 크기로 이루어진 직사각형이고 N,M을 입력 받는다.
N, M = map(int,input().split())

# (A,B) A는 북쪽으로 부터 떨어진 칸의 갯수
# B는 서쪽으러 부터 떨어진 칸의 개수

# 원점은 0,0이다.

#캐릭터는 메뉴얼 대로 움직인다.

# 메뉴얼 -> 핵심 로직 (메뉴얼을 코드로 구현하면된다)
# 1. 현재 위치 방향을 기준으로 왼쪽 방향부터 갈 곳을 정한다
# 2. 바로 왼쪽 방향에 가보지 않은 칸이 존재시, 왼쪽으로 회전한 후 한칸
# 전진한다. 가보지않은 칸이 없다면 왼쪽으로만 회전하고 1번으로 돌아간다.
# 가본 칸과 가보지 않은 칸을 구분하도록 해야한다

d = [[0] * M for _ in range(N)]
# 3. 네 방향 모두 가본 칸이거나 바다인 칸의 경우 방향을 유지한채
# 1로 돌아간다. 뒤쪽 방향이 바다 칸인 경우라 뒤로 갈 수 없을 시
# 움직임을 멈춤

# 입력조건
# 1. N,M을 입력 받는다. N <=3 M <= 50
# 2. 캐릭터 초기 좌표 A,B 바라보는 방향 d를 공백으로 구분하여 입력받는다
# 북 : 0 동 : 1 남 : 2 서 : 3

# 이러한 순서는 괜히 준 것이 아니다.
#초기 위치는 육지이고, 역시 밞은 땅이니 1로 초기화 한다.
x, y, direction = map(int, input().split())
d[x][y] = 1
# 시뮬레이션 문제에서는 이러한 정보를 바탕으로 dx,dy를 작성한다
# 북 동 남 서 기준으로 움직일 수 있는 list를 작성한다
# 북, 남은 A좌표(x)에 영향을 미치며 동 ,서는 B좌표(y)에 영향을 미친다
# 따라서 x좌표에 영향을 미치는 북남과 동서를 분리해서 생각해야 하며
# 이러한 로직은 문제에서 주어진 0 1 2 3에 영감을 받아
# dx = [-1, 0, 1, 0]
# dy = [0,1,0,-1]
#로 작성하여 dx[direction]을 실행할 시 방향에 따라 연산이 가능하도록 한다
# 0(북)일시 [-1,0] 1(동)일시 [0,1] 2(남)일시 [1,0] 3(서)일시 [0,-1] ㅇ;디/
# 맵에 육지 바다 정보를 입력한다. 육지 : 0 바다 : 1
# array = []
# for _ in range(N):
#     array.append(list(map(int, input().split())))

# 서쪽부터 동쪽 순서대로 입력한다.

#밞은 칸의 갯수를 출력한다
dx = [-1, 0, 1, 0]
dy = [0,1,0,-1]

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

count = 1
turn_times = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

While True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny]==0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_times = 0
    else:
        turn_times += 1
    if turn_times ==4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_times = 0

print(count)



