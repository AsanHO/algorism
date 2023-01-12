import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n,k = map(int,input().split())

from collections import deque

people = deque()
for i in range(n):
    people.append(i+1)

print(people)

count = 1
result = []

while people:
    item = people.popleft()
    print(item,count,k)
    if count == k:
        result.append(item)
        count = 1
    else:
        people.append(item)
        count += 1
        
    
print("<",end="")
print(", ".join(map(str,result)),end="")
print(">")