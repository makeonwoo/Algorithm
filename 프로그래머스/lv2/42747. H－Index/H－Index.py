def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break
    
    if max(citations) == 0:
        answer = 0
    elif answer == 0:
        answer= i+ 1
    return answer