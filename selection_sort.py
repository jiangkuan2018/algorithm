#coding=utf-8
# 选择排序
def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)): # range函数生产出一个索引数组，for in循环遍历数组拿到索引 对应数组的位置 第三个参数为步长相当于 +=5
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest)) # pop 默认删除列表最后一位，
  return newArr

arr = [5, 4, 7, 99, 77, 231, 435, 656]
# print arr.pop(2)
# print arr
print selectionSort(arr)
