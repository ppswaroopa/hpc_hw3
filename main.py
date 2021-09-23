def solution(list, num):
    a = 0
    b = 0
    result = []
    index_map = {}
    for i, ele in enumerate(list):
        difference = num - ele
        if difference in index_map:
            result.append(i)
            result.append(index_map[difference])
            break
        else:
            index_map[num] = i
    return a, b


numbers = [0, 21, 78, 19, 90, 13]
print(solution(numbers, 21))
print(solution(numbers, 25))