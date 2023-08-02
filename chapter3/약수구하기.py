# n, p입력 받기
a,b=map(int,input().split())
c=0

# b(순서) c<a (0과 입력수)
while b and c<a: #b가 0일시 종료시키기 위해서
    c+=1
    if a%c==0: #나머지가 0 이라면
        b-=1
print(0 if b else c)