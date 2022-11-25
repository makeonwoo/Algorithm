def solution(num, total):
    answer = []
    start = (2*total/num + 1 - num) / 2;
    for i in range(num):
        answer.append(start+i)
    return answer