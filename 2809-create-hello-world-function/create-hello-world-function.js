/**
 * @return {Function}
 */
var createHelloWorld = function() {
    const hello="Hello World"
    return function(...args) {
        return hello
    }
};
createHelloWorld()

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */