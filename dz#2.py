from random import randint
import operator


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        mid = int(len(lst) // 2)
        left = merge_sort(lst[:mid], compare)
        right = merge_sort(lst[mid:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


nums_list = [randint(0, 50) for i in range(50)]
print(merge_sort(nums_list))
