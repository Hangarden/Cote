money = int(input()) #금액 N
# print(money)

changes = [500, 100, 50, 10] #화폐종류 K
count = 0
#잔돈의 종류에는 500, 100, 50, 10이 있다 큰 순서대로 나열 되어 있어야 큰 순서대로 거스름돈을 거슬러 줄 수 있다

# for문을 돌면서 잔돈들이 들어가게 된다.

for coin in changes:
    # 동전 몇개가 필요한지 세는 것
    count += money // coin
    # 해당 코인으로 거슬러주고 나눈 나머지 돈
    money %= coin

print(count)