def solution(n,m):
    answer = []

    n,m = min(n,m), max(n,m)
    for i in range(n,1,-1):
        if n % i ==0 and m % i ==0:
            tmp = i
            answer.append(tmp)
            break
    else:
        answer.append(1)
    ma = m*n//answer[0]
    answer.append(ma)
    return answer