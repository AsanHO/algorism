import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T=int(input())

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans


def bino_coef_factorial(n, m):
    return factorial(n) // factorial(m) // factorial(n-m)

for _ in range(T):
    n,m = map(int,input().split())
    result = bino_coef_factorial(m,n)
    print(result)