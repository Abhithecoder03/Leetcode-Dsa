/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let temp=init
    let count=init
    console.log(init)
    return {
        increment:function(){
            count=count+1
            return count},

        
        decrement:function(){count=count-1
        return count},
        reset:function(){
            count=temp
            return count}
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */