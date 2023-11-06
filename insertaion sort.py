#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        y = i - 1
        while y >= 0 and key < arr[y]:
            arr[y + 1] = arr[y]
            y -= 1
        arr[y + 1] = key

my_list = [31, 94, 51, 88, 22]
insertion_sort(my_list)

print("Sorted array is:", my_list)