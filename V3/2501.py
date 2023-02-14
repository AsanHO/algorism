import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n,k = map(int,input().split())
k = k - 1 

medis = []

for i in range(1,n+1,1):
    if n % i == 0:
        medis.append(i)
try:    
    print(medis[k])
except:
    print(0)
    