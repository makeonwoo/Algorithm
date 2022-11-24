def solution(common):
    answer = 0
    tmp = 0
    f_tmp = 0
    c= 0
    i = len(common)-1
    if  common[i] - common[i-1] == common[i-1] - common[i-2]:
        return common[i]+(common[i] - common[i-1])
    else:
        return common[i]*(common[1]//common[0])