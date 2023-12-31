

# 첫줄 입력할 숫자 n을 입력한다
leng = int(input())
# 수열의 숫자들을 입력한다
a = list(map(int, input().split(" ")))
# 목표 숫자를 입력한다.
target = int(input())
#만족하는 쌍의 갯수를 카운트할 변수
count = 0
# 리스트의 처음부터 끝까지 숫자들을 순회하며 덧셈을 한다
# 0 부터 끝까지 더한뒤
# 1부터 끝까지 더하고

for i in range(leng):
    val = target - a[i]
    if a.count(val) != 0:
        count += 1
    else:
        pass

print(int(count/2))
# 시간복잡도 초과 (n^2)
for i in range(leng):
    for j in range(1,leng):
        value = a[i] + a[j]
        if value == target:
            count += 1
        else:
            pass

print(int(count/2))


# 이진탐색 구현
def Bsearch(start, end, key):
    # 시작이 끝보다 크면 0리턴
    if start > end:
        return 0

    # 중간값 구하기
    mid = (start + end // 2)

    ## 중간값이 찾고자하는 값과 같다면 1
    if seq(mid) == key:
        return 1
    ## 중간값이 찾고자 하는 값보다 크다면
    elif seq(mid) > key:
        # 중간값 부터 버리고 중간값 전부터 다시 탐색
        return Bsearch(start,mid-1,key)
    else:
        # 중간전 부터 버리고 중간값 이후부터 다시 탐색
        return Bsearch(mid + 1, end, key)

#입력할 숫자 n개를 입력받는다.
n = int(input())
#수열을 입력받는다.
seq = list(map(int, input().split(" ")))
#목표숫자를 입력받는다.
key = int(input())
#수의 쌍을 계산하기 위한 변수 초기화
count = 0

# 수열에있는 수를 하나씩 대입한다.
for num in seq:
    # 수열에 있는 수의 곱셈이 목표값인 경우 이진탐색에서 잘못 검색할 가능성이 있음으로 예외처리를 한다.
    if (num * 2 == key):
        continue
        #0부터 리스트 끝까지 목표 숫자가 존재하는지 이진탐색을 한다. 이진탐색의 시간복잡도는 nlogn
    count += Bsearch(0,len(seq) -1, key - num)

#리스트에 있는 모든 수를 검사함으로 2를 나눠주어야 한다.
print(count // 2)


# 목표숫자와 값이 같다면 카운트에 +1을 한다.


#투포인터 풀이
#입력할 숫자 n개를 입력받는다.
n = int(input())
#수열을 입력받는다.
seq = list(map(int, input().split(" ")))
#목표숫자를 입력받는다.
key = int(input())
#수의 쌍을 계산하기 위한 변수 초기화
count = 0

i = 0
j = len(seq) -1

# i와 j가 같아진다면 투포인터가 겹치는 시점. 모두 탐색했으니 종료해야한다.
while i != j:
    #i와 j의 합이 key값이 같아진다면 카운트를 1올리고 i를 오른쪽으로 이동시킨다.
    if seq[i] + seq[j] == key:
        count += 1
        i += 1
    # i와 j의 합이 key값보다 크다면 j를 왼쪽으로 이동시킨다.
    if seq[i] + seq[j] > key:
        j -= 1
    # #i와 j의 합이 key값이 작아진다면 i를 오른쪽으로 이동시킨다.
    if seq[i] + seq[j] < key:
        i += 1

print(count)

# 접근법  n의 범위가 100000 임으로 시간복잡도가 nlogn 이여야 한다.
# nlogn인 알고리즘은 투포인터, 이진정렬 알고리즘이 있다. 두 알고리즘을 통해 문제를 접근할 방식을 탐색한다.
# 양쪽부터 탐색해서 더한 값이 목표값과 같다면 +1
# 목표값보다 크다면 오른쪽 포인터를 왼쪽으로 1만큼 이동
# 목표값보다 작다면 왼쪽 포인터를 오른쪽으로 1만큼 이동
# 둘의 포인터 값이 같다면 종료!

n = int(input())
x = list(map(int, input().split()))
target = int(input())
count = 0

i = 0
j = len(x) -1

while i != j:
    if x[i] + x[j] == target:
        count += 1
        i += 1
    elif x[i] + x[j] < target:
        i += 1
    else:
        j -= 1

print(count)
