"""
問題文
M 君は AtCoder に参加している選手の 1 人です。彼の最高レーティングは X です。
AtCoder では、最高レーティングに応じて選手に級位が与えられます。レーティング 400 以上 1999 以下については、以下の通りです。
400 以上 599 以下：8 級
600 以上 799 以下：7 級
800 以上 999 以下：6 級
1000 以上 1199 以下：5 級
1200 以上 1399 以下：4 級
1400 以上 1599 以下：3 級
1600 以上 1799 以下：2 級
1800 以上 1999 以下：1 級
M 君は何級を持っていますか。
"""

print(10-int(input())//200)

#別解
x = int(input())
if 400<=x<=599:
  print(8)
elif 600<=x<=799:
  print(7)
elif 800<=x<=999:
  print(6)
elif 1000<=x<=1199:
  print(5)
elif 1200<=x<=1399:
  print(4)
elif 1400<=x<=1599:
  print(3)
elif 1600<=x<=1799:
  print(2)
else:
  print(1)