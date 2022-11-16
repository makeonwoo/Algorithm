def solution(s,n):
    answer = ""

    for i in range(len(s)):
        tmp = ord(s[i])
        if (tmp >= 65 and tmp <=90) or (tmp >= 97 and tmp <=122):
            if (tmp <=90 and tmp+n>90) or (tmp<=122 and tmp+n>122):
                tmp -=26
            answer += chr(tmp+n)
        else:
            answer += s[i]

    return answer
