exports.binarySearch = function(target, arr){
  arr.sort();
  let indices = [0, arr.length -1]
  while (indices[1] - indices[0] > 0) {
    let middleI = Math.floor((indices[1] - indices[0])/ 2) + indices[0]
    let middle = arr[middleI]
    if (middle === target) {
      return middleI
    } else if (middle > target) {
      indices[1] = middleI - 1
    } else {
      indices[0] = middleI + 1
    }
  }
  if (arr[indices[0]] === target) {
    return indices[0]
  } else {
    return -1
  }
}


