/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    
    promise1 = new Promise(resolve => setTimeout(() => resolve(), millis)).then()
    return promise1

}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */