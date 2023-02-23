import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
h,m,s = map(int,input().split())
target_time = int(input())

print(h,m,s)
print(target_time)

#더할 시,분,초
add_minute = target_time//60
add_second = target_time%60

print("더할분 :",add_minute)
print("더할초 :",add_second)
m = m + add_minute
s = s + add_second
if s > 59:
    m = m + s//60
    s = s%60
    print(h,m,s)
if m > 59:
    h = h + m//60
    m = m%60
    print(h,m,s)
if h > 23:
    h = h%24
print(h,m,s)

