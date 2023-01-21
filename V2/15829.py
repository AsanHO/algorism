import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = int(input())
t_arr = list(map(str,input()))
alpha = {}
num = 1
for i in range(97,123):
    alpha[chr(i)] = num
    num += 1 
num = 0
result = 0
for i in t_arr:
    if i in alpha:
        result = result + alpha[i]*(31**num)
    num +=1
print(result%1234567891)