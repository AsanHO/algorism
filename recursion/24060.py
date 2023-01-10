import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T,num=map(int,input().split())
arr=list(map(int,input().split()))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = (len(arr)+1)//2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])
    i,j=0,0
    arr2 = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr2.append(l[i])
            ans.append(l[i])
            i+=1
        else:
            arr2.append(r[j])
            ans.append(r[j])
            j+=1
    while i < len(l):
        arr2.append(l[i])
        ans.append(l[i])
        i+=1
    while j < len(r):
        arr2.append(r[j])
        ans.append(r[j])
        j+=1
    return arr2
            
ans = []
merge_sort(arr)
if len(ans) < num :
    print(-1)
else:
    print(ans[num-1])