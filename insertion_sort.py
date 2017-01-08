def insertion_sort(list):
    for j in range(1, len(list)):
        i = j
        current_value = list[j]
        while current_value < list[i-1] and i > 0:
                list[i] = list[i-1]
                i -= 1
        list[1] = current_value

list = [4, 8, 1, 3, 0, 9, 1, 2, 10, 455, 7, 2]
insertion_sort(list)
print(list)
