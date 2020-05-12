// 交集
function intersection() {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    return args.reduce(function (acc, curr) {
        return acc.filter(function (accItem) {
            return curr.includes(accItem);
        });
    });
}
// 并集
function sum() {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    return args.reduce(function (acc, curr) {
        curr.forEach(function (currItem) {
            if (!acc.includes(currItem)) {
                acc.push(currItem);
            }
        });
        return acc;
    }, []);
}
console.log(intersection([3, 4, 5], [4, 5, 6,], [5, 6, 7]));
console.log(sum([3, 4, 5], [4, 5, 6,], [5, 6, 7]));
