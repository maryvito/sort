

def binar_search(alist, item, first, last):

    midpoint = (last+first)//2
    if first > last:
        return False
    elif alist[midpoint] == item:
        return True, midpoint
    elif item < alist[midpoint]:
        last = midpoint - 1
    else:
        first = midpoint + 1
    return binar_search(alist, item, first, last)


list = [1, 8, 17, 45, 111, 254, 588, 999]
list.sort()
print(binar_search(list, 19, 0, len(list)-1))




