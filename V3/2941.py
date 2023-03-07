import sys
os = sys.platform
if os != "linux":
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input = open("example.txt", "rt").readline
else:
    input = sys.stdin.readline

avg, track_count = map(int, input().split())
""" 만약 (올린 후의)평균이 24가 나왔다면, 올림을 안했을 때의 평균이 23일 때의 저작권 곡에서

딱 1권을 더했을 때의 곡이 23.xxx 가 될 것이고, 이것을 올림하면 24가 될 것이므로,

이 때의 곡의 개수가 평균이 24인 곡의 갯수에서 최소가 될 것이므로, 이것을 구해주면 된다. """
track_count -= 1
melody_count = avg * track_count + 1

print(melody_count)
