/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    res=[]
    arr.forEach((ele,i)=>{
      if(fn(ele,i)){
        res.push(arr[i])
      }
    })
    return res
};