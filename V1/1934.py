import sys

os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

t = int(input())
    
def gcd_v2(a, b) :
    alist = []
    maX = 0
    # 1부터 자기 자신까지 나누어떨어지는 수는 삽입
    for i in range(1,a):
        if a % i == 0:
            alist.append(i)
        i = i +1
    # b를 나누어지는 수로 나누어떨어진다면 maX변경
    for item in alist:
        if b % item == 0:
            maX = item
    return maX

for _ in range(t):
    a,b = map(int,input().split())
    aa,bb=a,b

    while a!=0:
        b = b % a 
        a,b = b,a        

    print(aa*bb//b)