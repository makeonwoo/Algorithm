def solution(nums):
    answer = 0
    li = list(set(nums))
    if len(li) > len(nums)/2:
        answer = len(nums)/2
        return answer
    return len(li)