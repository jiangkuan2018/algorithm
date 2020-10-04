Function.prototype.call2 = function(context) {
  var context = context || window
  context.fn = this
  var args = []
  for (var i=1, len = arguments.length; i < len; i++) {
    args.push('arguments['+ i +']')
  }
  var res = eval('context.fn('+args+')') // 数组会自动展开 array + string [1,2,3] + '' = 1,2,3
  delete context.fn
  return res
}

Function.prototype.apply2 = function(context, arr) {
  var context = context || window
  context.fn = this
  var res;
  if (!arr) {
    res = context.fn()
  } else {
    var args = []
    for (var i=0,len = arr.length; i<len;i++) {
      args.push('arr[' + i + ']')
    }
    res = eval('context.fn(' + args + ')')
  }
  delete context.fn
  return res
}

Function.prototype.bind2 = function(context) {

}

const obj2 = {
  x: 42,
  getX: function() {
    return this.x
  }
}

const getx = obj2.getX.bind(obj2)
// 赋值操作符会使用GetValue计算出表达式的值，而不是返回Reference类型，所以getx是得到了obj2.getX的值
// 根据this的判断情况 ref不是一个Reference的话 this为 undefined 非严格模式下 undefined会指向window

console.log(obj2.getX(), getx())

const obj = {
  value: 'hello'
}

function func(name, age) {
  console.log(this.value, name, age)
  return 'world'
}

func.call2(obj, 'jk', 100)
func.apply2(obj, ['jk', 200])
