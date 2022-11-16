def solution(n):
    li = [0 for _ in range(n+1)]
    li[0] = 0
    li[1] = 1
    for i in range(2, n+1):
        li[i] = li[i-2] + li[i-1]
    answer = li[n]
    return answer % 1234567