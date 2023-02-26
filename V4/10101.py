import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b & b == c:
        print("Equilateral")
    elif a == b or b == c  or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

    