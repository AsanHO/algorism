import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
n,m=map(int,input().split())

mtr=[]
cnt=[]
for i in range(n):
    mtr.append(input())
    
for a in range(n-7):
    for b in range(m-7):#8*8로 자르기 위해, -7해준다. 안해주면 인덱스 오류
        # 10 * 13의 경우 2*5만 해주면 끝남
        w_index=0 #흰색으로 시작
        b_index=0 #검은색으로 시작
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:#행렬인덱스 합이 짝수인 경우
                    if mtr[i][j]!='W':#W가 아니면, 즉 B이면
                        w_index+=1#W로 칠하는 갯수
                    else:#W일 때
                        b_index+=1#B로 칠하는 갯수
                else:#홀수인 경우
                    if mtr[i][j]!='W':#W가 아니면, 즉 B이면
                        b_index+=1#B로 칠하는 갯수
                    else:
                        w_index+=1#W로 칠하는 갯수
                print(mtr[i][j],w_index,b_index)
                  
        cnt.append(w_index) #W로 시작할 때 경우의 수
        cnt.append(b_index) #B로 시작할 때 경우의 수
print(min(cnt))
""" n,m = map(int,input().split())
#n행 m열
t = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    t[i] = list(str(input().strip()))
print(t)
compare1 = [
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","B","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
    ["W","B","W","B","W","B","W","B",],
    ["B","W","B","W","B","W","B","W",],
]
compare2 = list(reversed(compare1))

print(compare1)
print(compare2) """