def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + left[left_index:] + right[right_index:]


def sort_merge(array):
    length = len(array)
    if length <= 1:
        return array
    left = sort_merge(array[0:length//2])
    right = sort_merge(array[length//2:])
    return merge(left, right)


'''
Сортировка слиянием имеет сложность nlog n,
такую же сложность имеет быстрая сортировка,
но только в среднем или лучшем случае.
Так как на вход может поступить любой массив чисел,
то лучше выбрать стабильный способо сортировки.
'''
