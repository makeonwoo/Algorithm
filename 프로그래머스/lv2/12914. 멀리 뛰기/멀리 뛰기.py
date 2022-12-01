def solution(n):
    for i in range(3,n+2):
        li.append((li[i-1]+li[i-2])%1234567)
    return li[n+1]
li = [0,1,1]