import sys
from collections import Counter
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

burgers = []
burgers.append(int(input()))
burgers.append(int(input()))
burgers.append(int(input()))
drinks = []
drinks.append(int(input()))
drinks.append(int(input()))

set_menu = []
for burger in burgers:
    for drink in drinks:
        set_menu.append(burger+drink-50)
        
print(min(set_menu))