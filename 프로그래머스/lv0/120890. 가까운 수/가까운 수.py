def solution(array, n):
    answer = 0
    for i in array:
        if abs(n-i) < abs(answer-n):
            answer = i
        elif abs(n-i) == abs(answer-n):
            answer = min(i,answer)
    return answer