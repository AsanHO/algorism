import sys

os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

target = int(input())

cars = list(map(int,input().split(" ")))

result = 0
for car in cars:
    if target == car:
        result += 1

print(result)