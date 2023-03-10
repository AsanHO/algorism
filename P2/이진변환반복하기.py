def solution(s):
    total_zero_count = 0
    convert_count = 0
    while s != "1":
        s, zerocount = binary_converter(s)
        convert_count += 1
        total_zero_count += zerocount
    return [convert_count, total_zero_count]


def binary_converter(s):
    zero_count = s.count("0")
    s = str(bin(len(s.replace("0", ""))))
    s = s.replace("0b", "")
    return s, zero_count


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
