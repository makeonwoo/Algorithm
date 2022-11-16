def solution(a, b):
    tmp = 0
    s = ['FRI', 'SAT', 'SUN', 'MON', 'TUE','WED','THU']
    a-=1
    while a:
        if a%2 ==0 and a < 8:
            if a!=2:
                tmp+=30
            else:
                tmp+=29
        elif a%2 == 0 and a >= 8:
            tmp += 31
        elif a%2 == 1 and a < 8:
            tmp+=31
        else:
            tmp+=30
        a-=1
    print(tmp)
    answer = s[(tmp+b-1)%7]
    print(answer)
    return answer