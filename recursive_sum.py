arr = [1, 3, 7, 11, 30]
def sum(arr):
  if len(arr) == 0:
    return 0
  else:
    num = arr[0]
    arr.pop(0)
    return num + sum(arr)

# print sum(arr)
# arr2 = [1, 3, 100, 11, 8]
# def find_biggest(arr):
  