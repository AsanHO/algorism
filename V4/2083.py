import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline


while True:
    name,age,weight = map(str,input().split())
    age = int(age)
    weight = int(weight)
    
    if name == "#":
        break
    if age > 17 or weight >=80:
        print(name, "Senior")
    else:
        print(name, "Junior")
    