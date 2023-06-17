arr = ["3", "34"]
arr2 = [3, 30, 34, 5, 9]
print(sorted(arr))
print(arr2[3:])
print(sorted(arr2))
# 최대수가 1000이므로
arr2.sort(key=lambda x: (str(x)*3)[:3], reverse=True)
print(arr2)
if [1, 2] in [1, 3, 4]:
    print("hi")
