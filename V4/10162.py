import sys
from string import ascii_lowercase
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

target = int(input())

a,b,c = 300, 60, 10

a,target= divmod(target,a)[0],divmod(target,a)[1]
b,target= divmod(target,b)[0],divmod(target,b)[1]
c,target= divmod(target,c)[0],divmod(target,c)[1]

if target != 0 or a+b+c ==0:
    print(-1)
else:
    print(a,b,c)    