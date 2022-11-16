def solution(progresses, speeds):
    n = len(progresses)
    ls = [100 - progresses[i] for i in range(n)]
    l_time = []
    for i in range(n):
        tmp = ls[i]/speeds[i]
        if tmp != int(tmp):
            tmp +=1
        l_time.append(int(tmp))

    answer = []
    c = 1
    l = l_time[0]
    for i in range(1,n):
        if l >=l_time[i]:
            c +=1
        else:
            answer.append(c)
            l = l_time[i]
            c=1
    answer.append(c)
    return answer