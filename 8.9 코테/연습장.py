N, K = map(int, input().split())
# 1부터 N까지 숫자 리스트를 생성한다
A = list(range(1,N+1))
print(A)
# 저장할 리스트가 필요하다
result = []
# k번째 순서의 인덱스를 pop한 뒤 리스트에 저장한다.
pointer = 0
while A:
    # 포인터를 이동시켜야 한다.
    pointer += (K - 1)
    if pointer > len(A):
        pointer = pointer%len(A)
    # k번째 순서의 인덱스를 pop한 뒤 리스트에 저장한다.
    result.append(str(A.pop(pointer)))
print("<", ", ".join(result)[:], ">", sep='')
    # 이후에는 pop한 A리스트의 3번 인덱스 이후로 3번을 더 세야 한다. 2 5 1 6 4 0 3   +3 -4 +5 -2 -4 +3
    # 원형리스트를 구현해서 pop한 인덱스 다음으로 부터 3칸을 반복해야한다.

    # 인덱스를 하나를 줄여야 한다.


#
# 1,2,3,4,5,6,7,8  3
#
# 3, 6, 1, 5, 2, 1, 4, 8
#
#
# 1,2,4,8