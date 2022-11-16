def solution(N, stages):
    clear = [0 for _ in range(N)]
    fa = [0 for _ in range(N)]
    result = [0 for _ in range(N)]
    for j in range(1,N+1):
        for i in stages:
            if(i == j):
                clear[j-1] += 1

    temp = 0
    for k in range(N):
        if (len(stages)-temp) >0:
            fa[k] = (clear[k]/(len(stages)-temp),k+1)
            temp += clear[k]
        else :
            fa[k] = (0,k+1)
    fa.sort(key=lambda x: (-x[0], x[1]))

    for m in range(N):
        result[m] = fa[m][1]

    return result