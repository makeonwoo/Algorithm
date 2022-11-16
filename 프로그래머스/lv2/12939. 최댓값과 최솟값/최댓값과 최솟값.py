def solution(s):
    s = s.split(" ")
    i_list = list(map(int,s))
    print(s)
    answer = ''
    answer = str(min(i_list))+ " " + str(max(i_list))
    return answer