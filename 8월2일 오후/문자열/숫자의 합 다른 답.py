## SUM 함수 이용
n = input()

print(sum(map(int,input()))) # map함수에도 sum을 적용할 수 있다.

print(map(int,input())) #map을 만들수 있다 한줄 코딩으로

## for문 이용

n = input()
nums = input() #54321입력시
total = 0
for i in nums : #for 문자열 사용시 가능 5,4,3,2,1이 for문을 통해 들어감
    total += int(i)  # total= total+int(i)
print(total)

## for문이용 - 내 문제풀이와 유사
n = input()
nums = input()
total = 0
for i in range(n) :  # 0부터 n-1까지 굳이 0,를 안써줘도 됨
    total += int(nums[i])
print(total)