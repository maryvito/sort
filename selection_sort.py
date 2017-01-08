def selection_sort(list):

    for j in range(len(list)-1, 0, -1):
        index_max = 0
        for i in range(1, j+1):
            if list[index_max] < list[i]:
                index_max = i
        list[index_max], list[j] = list[j], list[index_max]

list = [4, 8, 1, 3, 0, 9, 1, 2, 10, 455, 7, 2]
selection_sort(list)
print(list)