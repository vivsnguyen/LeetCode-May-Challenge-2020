// /**
//  * @param {string} J
//  * @param {string} S
//  * @return {number}
//  */

var numJewelsInStones = function(J, S) {
    jewels = 0
    const setJ = new Set(J);
    
    for (const s of S) {

        if (setJ.has(s)) {
            jewels += 1;
        }
        
        // setJ.has(s) ? jewels + 1 : jewels + 0;
    }
    
    return jewels;
};