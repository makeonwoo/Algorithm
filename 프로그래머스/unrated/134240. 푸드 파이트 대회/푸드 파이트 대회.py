def solution(food):
    answer = ''
    count = -1
    tmp =""
    t_list = []
    for i in food:
        count+=1
        if i > 1:
            if i %2 != 0 : i-=1
            for _ in range(i//2):
                tmp += str(count)
            t_list.append(tmp)
        tmp=""
    for i in t_list:
        answer+= i
    answer+="0"
    for i in range(len(t_list)-1,-1,-1):
        answer+= t_list[i]
    return answer