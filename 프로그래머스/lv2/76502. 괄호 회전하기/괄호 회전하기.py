def solution(s):
  answer = 0
  tmp = s
  for i in range(len(s)):
    tmp = tmp[1:] + tmp[:1]
    if ch(tmp) :
      answer+=1
  return answer

def ch(s):
    str = [i for i in s]
    chek = []
    for i in str:
      if not chek:
        if i == "(" or i == "{" or i == "[":
          chek.append(i)
        else:
          return False
      else:
        if i == "(" or i == "{" or i == "[":
          chek.append(i)
        elif i == "]":
          tmp = chek.pop()
          if tmp == "[":
            continue
          else:
            return False
        elif i == "}":
          tmp = chek.pop()
          if tmp == "{":
            continue
          else:
            return False
        elif i == ")":
          tmp = chek.pop()
          if tmp == "(":
            continue
          else:
            return False
    if chek:
      return False
    return True