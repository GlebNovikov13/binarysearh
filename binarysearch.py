def bc(list, item):
    low = 0
    height = len(list)
    while low<height:
        mid = int((low+height) / 2)
        if(list[mid]==item):
            return item
        if(item>list[mid]):
            low = mid+1
        else:
            height = mid-1
    return None


a = [1, 4, 3, 8]
a.sort()
print(a)
print(bc(a, 9))