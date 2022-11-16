def solution(s):
    str = [i for i in s]
    chek = []
    for i in str:
        if not chek:
            if i =="(":
                chek.append(i)
            else:
                return False
        else:
            if i == "(":
                chek.append(i)
            else:
                chek.pop()
    if chek:
        return False
    return True