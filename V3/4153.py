import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

while True:
    nums= list(map(int,input().split()))
    max_num = max(nums)
    if sum(nums) == 0:
        break
    nums.remove(max_num)
    if ((nums[0]**2) + (nums[1]**2)) == max_num**2:
        print("right")
    else:
        print("wrong")


