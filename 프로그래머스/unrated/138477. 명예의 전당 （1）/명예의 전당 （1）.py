def solution(k, score):
    answer = []
    li = []
    for i in score:
        li.append(i)
        li.sort()
        if len(li)>k:
            del li[0]
        answer.append(li[0])
    return answer