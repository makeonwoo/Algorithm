def solution(n):
    for i in range(3,n+2):
        li.append((li[i-1]+li[i-2])%1234567)
    return li[n+1]
li = [0,1,1]

def t(n,a):#피보나치수인걸 알아낸 방법
    if n == a:
        return li.append(a)
    elif n<a:
        return
    else:
        t(n,a+1)
        t(n,a+2)
