def quicksort(array):
  if len(array) < 2:
    return array
  else:
    piovt = array[0]
    less = [i for i in array[1:] if i <= piovt]
    greater = [i for i in array[1:] if i > piovt]
    return quicksort(less) + [piovt] + quicksort(greater)
# print quicksort([10, 5, 2, 4])

def multip(arr):
  newArr = arr
  for i in range(len(arr)):
    print arr[i]
    # print newArr


multip([2, 3, 7, 8, 10])