import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n = int(input())

result = 1
def factorial(n):
    global result
    if n <= 1:
        print(result)
        return
    result = result * n
    factorial(n-1)
    
factorial(n)