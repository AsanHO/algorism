import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

#이진탐색을 한후, 해당 값을 키값으로 사용ㅐ 해싱
a.sort()
result = []
def bs (m,a):
    for target in m:
        start = 0
        end = len(a) - 1
        while start <= end:
            mid = (start + end) //2    
            if a[mid] == target:        
                
                break
            elif a[mid] < target:
                start = mid + 1 
            else:
                end = mid - 1
        


bs(m,a)

""" # 실버 4
# 시간초가 나기 때문에 중복 수 제거해야함
import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))

M = int(input())
m_arr = list(map(int, input().split()))
for m in m_arr:
    if m in arr:
        print(1)
    else:
        print(0) """