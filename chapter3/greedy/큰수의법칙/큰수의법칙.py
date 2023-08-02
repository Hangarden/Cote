# 입력에는 N, M, K 를 입력받는다. N은 숫자들의 개수, M은 연산해야하는 횟수, K는 중복으로 사용 가능한 횟수
# K는 항상 M보다 작거나 같다. -> 코드레벨에서는 구현할 필요는 없다.
# 배열에 들어가는 숫자 역시 코드레벨에서 에러를 구현할 필요는 없다

# 우선 N,M,K를 작성한다


#sort알고리즘을 통해 가장 큰 순서로 정렬한다


#0번째 인덱스와 첫번째 인덱스를 추출한다.

#M과 K에 따라 다르게 연산되는데 K만큼 0번째 인덱스를 반복해서 더한 뒤 첫번째 인덱스를 더한다.

# 2 4 5 4 6
# 5 8 3 경우
# 6 6 6 5 6 6 6 5

# 2 4 5 4 6
# 5 7 3
# 6 6 6 5 6 6 6

# 6 6 6 5 6 6

# 간단하게 생각해보면 일단 K와 M을 판단한 뒤 같다면 M만큼 더하면 되고
# M이 더 크다면 K+1 만큼 더한 뒤 M -= K + 1 을 실행한다

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -=1
    if M == 0:
        break
    result += second
    M -= 1

print(result)

