def solution(number, limit, power):
  l = [1]
  c = 0
  for i in range(2, number + 1):
    for j in range(1, int(i**(1/2))+1):
      if j * j == i and i != 1:
        c += 0.5
      elif i % j == 0:
        c += 1
    c *= 2
    if c > limit:
      c = power
    l.append(int(c))
    c = 0
  answer = sum(l)
  return answer