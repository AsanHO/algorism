import sys
from string import ascii_lowercase
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

s = list(str(input()))
alphabet_list = list(ascii_lowercase)
result = [0 for i in range(len(alphabet_list))]
for i in range(len(alphabet_list)):
    for item in s:
        if alphabet_list[i] == item:
            result[i] += 1
            
for i in result:
    print(i,end=" ")
