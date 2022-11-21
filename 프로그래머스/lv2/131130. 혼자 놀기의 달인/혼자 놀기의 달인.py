def solution(cards):
    li = [[] for i in range(len(cards))]
    ck,l_len = [],[]
    n = len(cards)
    i=0
    c=0
    l_c = 0
    while n != l_c:
        if cards[i-1] not in ck:
            li[c].append(cards[i-1])
            ck.append(cards[i-1])
            i = cards[i-1]
            l_c+=1
        else:
            c+=1
            i = list(set(cards) - set(ck))[0]
    for i in range(n):
        l_len.append(len(li[i]))
    l_len.sort(reverse=True)
    return l_len[0]*l_len[1]