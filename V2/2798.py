import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n,m= map(int,input().split())

nums = list(map(int,input().split()))

#경우의 수 계산
from itertools import *
jacks = list(combinations(nums,3))
result = []
for jack in jacks:    
    if sum(jack) <= m:
        result.append(sum(jack))

result.sort()
print(result[-1])