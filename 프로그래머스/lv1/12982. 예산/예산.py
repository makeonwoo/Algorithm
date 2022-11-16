def solution(d, budget):
    d.sort()
    s = 0
    answer = 0
    for i in d:
        if budget>=s+i:
            s+=i
            answer += 1
    print(answer, s)
    return answer