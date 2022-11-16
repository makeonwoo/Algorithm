def solution(n, s):
    answer = []
    tmp =0
    num = int(s/n)
    if s <2 or n>s:
        return [-1]
    if s%n ==0:
        for i in range(n):
            answer.append(num)
    else:
        tmp = s%n
        for i in range(n):
            if tmp>0:
                answer.append(num + 1)
                tmp -= 1
            elif tmp<0:
                answer.append(num + tmp)
            else:
                answer.append(num)
    answer.sort()
    return answer