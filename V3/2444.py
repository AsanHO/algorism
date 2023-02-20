import sys

os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

target = int(input())
count_list = []
for i in range(target):
    i += 1
    count = 2*i-1
    count_list.append(count)
re_count_list = list(reversed(count_list))
del re_count_list[0]
last = count_list[-1]
for i in count_list:
    blank_count = int((last - i) / 2)
    blank = " "*(blank_count-1)
    star = "*"*i
    if i == last:
        print(star)
    else:
        print(blank,star)
for i in re_count_list:
    blank_count = int((last - i) / 2)
    blank = " "*(blank_count-1)
    star = "*"*i
    if i == last:
        print(star)
   
    else:
        print(blank,star)