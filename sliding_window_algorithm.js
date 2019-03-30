// 滑动窗口算法 规定长度 在arr中最大的连续值
var arr = [100, 50, 200, 300, 150]

function maxSum(arr, k) {
  const n = arr.length
  if (n < k) {
    return -1
  }
  let maxSum = 0
  for (let i = 0; i < k; i++) {
    maxSum += arr[i]
  }
  let sum = maxSum
  for (let i = k; i < n; i++) {
    console.log(arr[i], arr[i - k], i)
    // 新窗口的和 = 前一个窗口的和 + 新进入窗口的值 arr[i] - 移出窗口的值 arr[i - k]
    sum += arr[i] - arr[i - k]
    maxSum = Math.max(maxSum, sum); //  每次保留最大值
  }
  console.log(maxSum)
}

maxSum(arr, 2)