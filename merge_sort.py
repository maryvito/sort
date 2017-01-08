def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2

        leftparth = alist[:mid]
        rightparth = alist[mid:]

        merge_sort(leftparth)
        merge_sort(rightparth)

        i=0
        j=0
        k=0

        while i < len(leftparth) and j < len(rightparth):
            if leftparth[i] < rightparth[j]:
                alist[k] = leftparth[i]
                i += 1
                k += 1
            else:
                alist[k] = rightparth[j]
                j += 1
                k += 1

        while i < len(leftparth):
            alist[k] = leftparth[i]
            i += 1
            k += 1

        while j < len(rightparth):
            alist[k] = rightparth[j]
            j += 1
            k += 1

list = [4, 8, 1, 3, 0, 9, 1, 2, 10, 455, 7, 2]
merge_sort(list)
print(list)