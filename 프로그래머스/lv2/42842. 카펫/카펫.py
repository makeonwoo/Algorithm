def solution(n,m):
    result = []
    r = n + m
    s = [1]
    for i in range(2,r+1):
        if r % i == 0 :
            s.append(i)
    re_s = sorted(s,reverse=True)
    for i in s:
        for j in re_s:
            if i>j:
                break
            ch = 2*i +2*j -4
            if ch == n and i * j == r:
                result=[j,i]
                
                break

    return result