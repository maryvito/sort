def quick_sort(list):
    quick_sort_helper(list, 0, len(list) - 1)

def quick_sort_helper(list, first, last):

   if first < last:
    middl = mid(list, first, last)

    quick_sort_helper(list, first, middl - 1)
    quick_sort_helper(list, middl + 1, last)

def mid(list, first, last):
    start = first
    sup_element = list[first]
    first += 1
    while first < last:
        while list[first] < sup_element:
            first += 1
        while list[last] > sup_element:
            last -= 1
        if first < last:
            list[first], list[last] = list[last], list[first]
    list[start], list[last] = list[last], list[start]
    return last




list = [4, 8, 1, 3, 0, 9, 1, 2, 10, 455, 7, 2]
quick_sort(list)
print(list)




