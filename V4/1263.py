import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline


while True:
    s = input().rstrip()
    if s == "#":
        break
    count = 0
    s = s.lower()
    for alpha in s:
        if alpha == "a" or alpha == "e" or alpha == "i" or alpha == "o" or alpha == "u":
            count += 1
    print(count)
        