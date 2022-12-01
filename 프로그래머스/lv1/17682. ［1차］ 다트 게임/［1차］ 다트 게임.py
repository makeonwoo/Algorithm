def solution(dartResult):
    tmp = 0
    point = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i-1].isdigit():
                tmp = int(str(tmp)+dartResult[i])
            else:
                point.append(tmp)
                tmp = int(dartResult[i])
        elif dartResult[i] == "S":
            tmp = tmp * 1
        elif dartResult[i] == "D":
            tmp = tmp * tmp
        elif dartResult[i] == "T":
            tmp = tmp * tmp *tmp
        elif dartResult[i] == "*":
            if len(point) <1:
                tmp = tmp*2
            else:
                tmp = tmp * 2
                point[(len(point)-1)] = point[(len(point)-1)]*2
        elif dartResult[i] == "#":
            tmp = -tmp
    point.append(tmp)
    return sum(point)