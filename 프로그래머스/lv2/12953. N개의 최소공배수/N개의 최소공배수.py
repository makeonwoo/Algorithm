def solution(arr):
    li = []
    temp = arr[0]
    for i in range(1,len(arr)):
        answer = gcd(temp, arr[i])
        temp = temp * arr[i] / answer
    return temp

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a