def solution(command: str) -> str:
  ret_com = ""
  for i in range(len(command)):
    if command[i] == "G":
      ret_com += "G"
    if command[i] == "(":
      if command[i + 1] == ")":
        ret_com += "o"
      elif command[i + 1] == "a" and command[i + 2] == "l" and command[i + 3] == ")":
        ret_com += "al"

  return ret_com

sol = solution("G()()()()(al)")
print(sol)
