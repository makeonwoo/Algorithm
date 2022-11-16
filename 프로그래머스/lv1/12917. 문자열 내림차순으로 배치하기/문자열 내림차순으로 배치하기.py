def solution(s):
    tmp= []
    answer = ""
    for i in range(len(s)):
        tmp.append(s[i])
    tmp.sort(reverse=True)
    for j in tmp:
        answer += j
    return answer