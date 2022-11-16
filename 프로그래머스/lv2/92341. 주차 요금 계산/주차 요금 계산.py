import math


def solution(fees, records):
    CarList = []
    H = []
    M = []
    InCar = []
    answer = []

    for i in range(len(records)):
        f = records[i].split()
        if f[1] not in CarList:
            CarList.append(f[1])
            answer.append(0)
    CarList.sort()
    for i in range(len(records)):
        f = records[i].split()
        h = f[0][:2]
        m = f[0][3:]
        if f[2] == "IN":
            InCar.append(f[1])#들어올때
            H.append(h)
            M.append(m)

        else:
            tmp = InCar.index(f[1])
            answer[CarList.index(f[1])]+= int(h)*60 - int(H[tmp])*60
            answer[CarList.index(f[1])] += int(m) - int(M[tmp])
            del H[tmp]
            del M[tmp]
            del InCar[tmp]
    while len(InCar) != 0:
        Last = CarList.index(InCar.pop())
        answer[Last] += 23 * 60 - int(H.pop()) * 60
        answer[Last] += 59 - int(M.pop())

    for i in range(len(answer)):
        if answer[i] <fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1]+math.ceil((answer[i] - fees[0])/fees[2]) * fees[3]

    return answer