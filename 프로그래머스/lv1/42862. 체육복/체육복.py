def solution(n, lost, reserve):
    answer = 0
    m = [1 for i in range(n)]
    for i in lost:
        m[i-1] -= 1
    for i in reserve:
        m[i-1] += 1
    for i in range(len(m)):
        if m[i] == 0:
            if i>0 and i<len(m)-1:
                if m[i-1] ==2:
                    m[i] =1
                    m[i-1] -=1
                elif m[i+1] ==2:
                    m[i] =1
                    m[i+1] -=1
            elif i == len(m)-1:
                if m[i-1] ==2:
                    m[i] =1
                    m[i-1] -=1
            else:
                if m[i+1] ==2:
                    m[i] = 1
                    m[i + 1] -= 1
    answer = len(m) - m.count(0)
    return answer