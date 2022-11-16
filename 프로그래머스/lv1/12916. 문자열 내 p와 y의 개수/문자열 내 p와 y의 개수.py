def solution(s):
    p1 =s.count("p")
    p2 =s.count("P")
    y1 =s.count("y")
    y2 =s.count("Y")
    if p1+p2 == y1+y2:
        answer = True
    else:
        answer = False

    return answer