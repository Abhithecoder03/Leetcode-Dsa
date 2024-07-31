/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let call=0
    return function(...args){
        
        for(let i=0;i<1;i++){
            
           if(call==0 && i<1){
            
            call=1
            return fn(...args)
           
           
           }
          
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
