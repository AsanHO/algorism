import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = int(input())

stack =[]
for _ in range(T):
    i = int(input())
    if i == 0:
        stack.pop()
    else:
        stack.append(i)    
print(sum(stack))