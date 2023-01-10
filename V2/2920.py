import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

melody = list(map(int,input().split()))

result = ""
#한꺼번에 하지 말자.
for i in range(8):
    if i+1 == melody[i]:
        result = "ascending"
    else:
        result = ""
        break
if result == "":
    for i in range(8):
        if 8-i == melody[i]:
            result = "descending"
            continue
        else:
            result = "mixed"
            break
    
print(result)