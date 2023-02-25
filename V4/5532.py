import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
import math
print(L-max([math.ceil(a/c),math.ceil(b/d)]))


    