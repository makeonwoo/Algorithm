import math


def solution(n, words):
    ch = []
    turn = 0
    tmp = ""
    for i in words:
        if i in ch:
            turn+=1
            break
        if tmp == "":
            turn +=1
        elif tmp[len(tmp)-1] == i[0]:
            turn +=1
        else:
            turn +=1
            break
        ch.append(i)
        tmp = i
    else:
        return [0,0]
    if turn%n == 0:
        answer = [n,math.ceil(turn/n)]
    else:
        answer = [turn%n,math.ceil(turn/n)]

    return answer