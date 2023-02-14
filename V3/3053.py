import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

r = int(input())

import math
print(f"{math.pi * r * r:.6f}")
print(f"{2 * r * r:.6f}")
