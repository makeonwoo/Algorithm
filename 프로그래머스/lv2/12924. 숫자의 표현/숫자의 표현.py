def solution(n):
    answer = 0
    cnt = 0
    while cnt <n:
        cnt +=1
        sum = 0
        for i in range(cnt,n+1):
            sum += i
            if(sum == n):
                answer +=1
            elif sum > n:
                break
    return answer