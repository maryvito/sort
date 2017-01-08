def bubble_sort(list):
    for j in range((len(list)-1), 0, -1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

list = [4, 8, 1, 3, 0, 9, 1, 2, 10, 455, 7, 2]
bubble_sort(list)
print(list)