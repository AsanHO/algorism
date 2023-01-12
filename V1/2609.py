import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

a,b = map(int,input().split())

divisor = []
max_num = 0
for i in range(a):
    num = i +1
    if a % num == 0:
        if b % num == 0:
            max_num = num

print(max_num)
print(int(a*b/max_num))
