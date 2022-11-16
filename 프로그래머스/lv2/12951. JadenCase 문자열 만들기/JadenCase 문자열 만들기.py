def solution(s):
    tmp = s.split(" ")
    answer = ''
    for i in tmp:
        answer += i.capitalize() + " "
    answer = answer[:-1]
    return answer