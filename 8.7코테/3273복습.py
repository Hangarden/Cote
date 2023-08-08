# #투포인터
# n = int(input())
# x = list(map(int, input().split()))
# target = int(input())
# count = 0
#
# x.sort()
# i = 0
# j = len(x)-1
#
#
# while i != j:
#     if x[i] + x[j] == target:
#         count += 1
#         i += 1
#     elif x[i] + x[j] < target:
#         i += 1
#     else:
#         j -= 1
#
# print(count)
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