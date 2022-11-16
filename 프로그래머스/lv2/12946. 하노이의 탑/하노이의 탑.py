answer = []
def solution(n):
    ha(n,1,2,3)
    return answer

def ha(n, fr, tmp, to):
    if n == 1:
        answer.append([fr,to])
    else:
        ha(n-1,fr,to,tmp)
        answer.append([fr,to])
        ha(n-1,tmp,fr,to)