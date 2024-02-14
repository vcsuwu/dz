def bubble_sort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1],list1[j]
    return list1

def find_substring(prompt,text):
    indicies = []
    start_index = 0
    while True:
        index = text.find(prompt, start_index)
        if index == -1:
            break
        indicies.append(index)
        start_index = index + len(prompt)
    return indicies

list_sort = [1,3,5,3,6,6]
sorted_list = bubble_sort(list_sort)
print(find_substring("text","hello text text"))
print(sorted_list)