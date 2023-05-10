arr = ["3", "34"]
arr2 = [3, 30, 34, 5, 9]
arr2.sort(key=lambda x: str(x)*3, reverse=True)  # 사전식 정렬 - 파이썬 특징
print(sorted(arr))
print(sorted(arr2))
