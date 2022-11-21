def solution(n, k):
    answer = 0
    m = ""
    if k == 10:
        l = str(n).split("0")
    else:
        while n > 0:
            m = str(n % k) + m
            n = n// k
        l = m.split("0")
    l = [i for i in l if i]
    for i in l:
        if i != "1":
            tmp = int(i)
            for i in range(2, int(tmp ** 0.5) + 1):
                if tmp % i == 0:
                    break
            else:answer+=1
    return answer