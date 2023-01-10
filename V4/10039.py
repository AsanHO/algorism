import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

sum = 0
for i in range(5):
    num = int(input())
    if num < 40:
        num = 40
    sum +=num
    
print(int(sum/5))
