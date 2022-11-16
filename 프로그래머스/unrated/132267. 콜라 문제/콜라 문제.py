def solution(a, b, n):
    answer = 0
    while n>a-1:
        t = n // a # 10
        t = t*b
        answer += t
        t += n % a # 
        n = t
    return answer