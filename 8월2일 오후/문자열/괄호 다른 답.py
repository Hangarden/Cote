# 문제의 목적은 스택 자료구조를 얼마나 잘 활용하는지 판단하기 위해서.
#

T = int(input())

for i in range(T): # T번 입력받기 위해서 작성
    stack = [] #stack todtjd
    a=input()
    for j in a:
        if j == '(':
            stack.append(j) # '('를 추가
        elif j == ')': # ')'를 발견시
            if stack: #stack에 )가 있다면 pop을 통해서 소거함
                stack.pop()
            else: # 스택에 괄호가 없을경우 ()가 짝이 맞지 않는 경우임으로 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")