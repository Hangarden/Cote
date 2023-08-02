# 6665 6665
#만일 m과 k가 같다면 666까지만
#m이 더 크다면 6665가 반복 될 것이다.
#더 크다면 m - k+1을 반복하고, m<=k인 순간이 온다면 남은 m만큼만 해당 6665에서 짤려서 출력될 것이다.

n, m, k = map(int, input().split( ))
data = list(map(int, input().split( )))

data.sort()

