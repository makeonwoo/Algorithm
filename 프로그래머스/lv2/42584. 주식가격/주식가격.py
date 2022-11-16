def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        for j in range(i+1,n):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        if len(answer)<i+1:
            answer.append(n-(i+1))
    answer.append(0)
    return answer