import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=int(input())

count = 0
def recursion(s,  l,  r):
    global count
    count = count + 1 
    if l >= r:
        return 1;
    elif s[l] != s[r]:
        return 0;
    else :
        return recursion(s, l+1, r-1);

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1);

for i in range(T):
    e = (input().strip())
    print(isPalindrome(e), count)
    