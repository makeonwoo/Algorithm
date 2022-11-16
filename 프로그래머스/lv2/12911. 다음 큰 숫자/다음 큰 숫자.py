def solution(numbers):
    answer = []
    i = numbers + 1

    o_n = str(bin(numbers)).count("1")
    while True:
        o = str(bin(i)).count("1")
        if o_n == o :
            break
        i+=1
    answer = i
    return answer