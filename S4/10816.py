import sys
from collections import Counter
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

c= Counter(a)
print(c)
for i in m:
  if i in c:
    print(c[i], end=' ')
  else:
    print(0, end=' ')