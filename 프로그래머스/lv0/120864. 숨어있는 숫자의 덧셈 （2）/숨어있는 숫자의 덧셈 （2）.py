def solution(my_string):
    answer = 0
    t = ""
    for i in my_string:
        if i.isdigit():
            t+= str(i)
            print(t)
        else :
            if t != "":
                answer += int(t)
            t=""
    if t != "":
        answer += int(t)
    return answer