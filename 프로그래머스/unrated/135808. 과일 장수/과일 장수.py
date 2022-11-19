def solution(k, m, score):
    answer = 0

    score.sort(reverse=True)

    l = len(score)//m

    for i in range(1,l+1):
      answer = answer + score[(i*m-1)] * m

    return answer