import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

t = int(input())

import queue
cards = queue.Queue()

for i in range(t):
    cards.put(i+1)

#리스트를 쓰면 정렬이 너무 많이 일어남, 큐
while cards.qsize() != 1:
    cards.get()
    take = cards.get()
    cards.put(take)
    
print(cards.get())
