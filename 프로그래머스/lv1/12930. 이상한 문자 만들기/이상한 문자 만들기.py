def solution(s):
    answer = ''
    s = s.split(" ")
    index = 0
    for i in s:
        for j in i:
            if index % 2 ==0 :
                answer += j.upper()
            else:
                answer += j.lower()
            index+=1
        answer += " "
        index=0

    answer = answer[:len(answer)-1]
    return answer