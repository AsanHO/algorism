import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = int(input())
    
for i in range(1,T+1):
    ones = sum(map(int,str(i)))
    result = ones + i #자리수 더하기 #자기자신 더하기   
    if result == T:
        print(i)
        break
    if i == T:
        print(0)
    