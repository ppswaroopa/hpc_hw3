# Question 1

def solution(list, num):
    a = 0
    b = 0
    index_map = {}
    for i, ele in enumerate(list):
        difference = num - ele
        if difference in index_map:
            b = i
            a = index_map[difference]
            break
        else:
            index_map[ele] = i
    return a, b


numbers = [0, 21, 78, 19, 90, 13]
print("Solution:21:", solution(numbers, 21))
print("Solution:25:", solution(numbers, 25))