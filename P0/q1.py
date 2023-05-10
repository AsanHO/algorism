"""
자연수가 들어있는 배열 arr가 매개변수로 주어집니다. 
배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터 뒤에 중복되어 나타나는 숫자들
중복 횟수를 계산해서 배열로 return 하도록 solution 함수를 완성해주세요. 
만약 중복되는 숫자가 없다면 배열에 -1을 채워서 return 하세요.

▶입출력 예 #1
arr = [1, 2, 3, 3, 3, 3, 4, 4]에서 3은 4번, 4는 2번씩 나타나므로 [4, 2]를 반환합니다.
▶입출력 예 #2
arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]이면 2가 3회, 4가 2회, 5가 3회 나타나므로 [3, 2, 3]를 반환합니다. 
▶입출력 예 #3
[3, 5, 7, 9, 1]에서 중복해서 나타나는 숫자는 없으므로 [-1]을 반환합니다.
##### 제한사항
- 배열 arr의 길이는 1 이상 100 이하의 자연수입니다.
- 배열 arr의 원소는 1 이상 100 이하의 자연수입니다.
"""
from collections import Counter


def solution(nums):
    answer = []
    nums.sort()
    i = 0
    while i < len(nums)-1:
        num = nums[i]
        count = 1
        for j in range(i+1, len(nums)):
            if num == nums[j]:
                count += 1
        if count > 1:
            answer.append(count)
        i += count
    if len(answer) == 0:
        return -1
    else:
        return answer


print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
print(solution([3, 5, 7, 9, 1]))