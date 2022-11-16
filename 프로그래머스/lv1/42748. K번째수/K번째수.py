def solution(array, commands):
    answer = []
    tmp = []
    for i in range(len(commands)):
        print(i)
        for j in range(commands[i][0]-1,commands[i][1]):
            tmp.append(array[j])
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
        tmp = []

    return answer