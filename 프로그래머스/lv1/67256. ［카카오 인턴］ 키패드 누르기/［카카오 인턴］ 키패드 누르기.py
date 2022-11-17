def distance(p1, p2):  
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))
def solution(numbers, hand):
    answer = ''
    p=[]
    for j in range(4):
        for i in range(1,4):
            p.append({'id':i+j*3,'p':(j+1,i)})
    print(p)

    l_last, r_last = 10,12
    for i in numbers:
        print(i,"start")
        if i == 1 or i == 4 or i == 7:
            answer += "L"
            l_last = i
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            r_last = i
        else:
            if i == 0:
                i = 11
            tmp = (item for item in p if item['id'] == i)
            i_dict = next(tmp, False)
            print(i_dict['p'])
            tmp = (item for item in p if item['id'] == l_last)
            l_dict = next(tmp, False)
            tmp = (item for item in p if item['id'] == r_last)
            r_dict = next(tmp, False)
            l_tmp = distance(i_dict['p'],l_dict['p'])
            r_tmp = distance(i_dict['p'],r_dict['p'])
            if l_tmp > r_tmp :
                answer += "R"
                r_last = i
            elif l_tmp < r_tmp :
                answer += "L"
                l_last = i
            else:
                if hand == "left" :
                    l_last = i
                    answer += "L"
                else:
                    r_last = i
                    answer += "R"
    return answer
