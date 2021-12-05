import math
n = int(input())
m = math.ceil(n/1.08)
if n==math.floor(m*1.08):
  print(m)
else:
  print(":(")