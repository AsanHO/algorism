import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

T = int(input())
from collections import deque
prints = deque()



for _ in range(T):
    n,m = map(int,input().split())
    doc = list(map(int,input().split()))
    doc_index = list(range(len(doc)))
    doc_index[m] = "target"
    
    order = 0
    
    MAX = max(doc)
    for i in doc:
        print(i,MAX)
        if i == MAX:
            order+=1
            if doc_index[0] == "target":
                print(order)
                break
            else:
                doc.pop(0)
                
                doc_index.pop(0)
        else:
            doc.append(doc.pop(0))
            MAX = max(doc)
            doc_index.append(doc_index.pop(0))
    