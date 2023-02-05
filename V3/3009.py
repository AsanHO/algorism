import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline



xs=[]
ys=[]
for _ in range(3):
    x,y = (map(int,input().split(" ")))
    xs.append(x)
    ys.append(y)
    
x=0
y=0
if xs[0] == xs[1]:
    x = xs[2]
elif xs[0] == xs[2]:
    x = xs[1]
else:
    x = xs[0]
if ys[0] == ys[1]:
    y = ys[2]
elif ys[0] == ys[2]:
    y = ys[1]
else:
    y = ys[0]
    
print(x,y)