def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1],list1[j]
    return list1

list_sort = [1,3,5,3,6,6]
sorted_list = bubble_sort(list_sort)
print(sorted_list)