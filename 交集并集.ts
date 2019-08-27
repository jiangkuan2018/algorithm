// 交集
function intersection(...args: number[][]): number[] {
  return args.reduce((acc, curr) => {
    return acc.filter(accItem => {
      return curr.includes(accItem)
    })
  })
}
// 并集
function sum(...args: number[][]): number[] {
  return args.reduce((acc, curr) => {
    curr.forEach(currItem => {
      if (!acc.includes(currItem)) {
        acc.push(currItem)
      }
    })
    return acc
  }, [])
}

console.log(intersection([3, 4, 5], [4, 5, 6,], [5, 6, 7]))
console.log(sum([3, 4, 5], [4, 5, 6,], [5, 6, 7]))

