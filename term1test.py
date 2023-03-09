#first ques
a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:  # check if the input numbers are in non-decreasing order
  if a**2 + b**2 == c**2:
      print(f"{a} squared plus {b} squared is equal to {c} squared")
  elif a**2 + b**2 < c**2:
      print(f"{a} squared plus {b} squared is less than {c} squared")
  elif a**2 + b**2 > c**2:# 
      print(f"{a} squared plus {b} squared is more than {c} squared")
  else:
    print(f"{c} squared is greater than the sum of the squares of {a} and {b}")
