n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
  if a[i]%2!=0 and i%2==0:
    ans += 1
print(ans)