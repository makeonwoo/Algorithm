def solution(s):
    z_count = 0
    timer = 0
    while s!= "1":
        z_count += s.count("0")
        timer+=1
        s=s.replace("0","")
        s= bin(len(s))
        s= s[2:]
    answer = [timer,z_count]
    return answer