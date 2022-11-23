def solution(chicken):
    answer = 0
    while chicken >9:
        tmp = chicken//10
        answer += tmp 
        chicken = chicken%10 + tmp
    return answer