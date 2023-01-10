import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=int(input())

arr = []

for i in range(T):
    arr.append(int(input()))

#max,sort
arr.sort()
max = 0
for i in arr:
    max = max + i
#avg
avg = round(max/T)
print(avg)
#mean
mean = arr[int(T / 2)]
print(mean)
#mode
dic = {}
for i in arr:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
modes = []
count = 1
for i in dic:
    if dic[i] > count:
        modes = []
        modes.append(i)
        count = dic[i]
    elif dic[i] == count:
        modes.append(i)
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
#extent
extent = arr[-1] - arr[0]
print(extent)