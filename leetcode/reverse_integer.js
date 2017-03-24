/**
 * https://leetcode.com/problems/reverse-integer/
 * 
 * @param {number} x
 * @return {number}
 */
var MAX_INT32 = Math.pow(2,31) - 1;
var MIN_INT32 = Math.pow(2,31) * -1;
 
var reverse = function(x) {
    var numberChars = Array.from(String(x));
    var offset = 0;
    if (numberChars[0] === '-') {
        offset = 1;
    }
    var midpoint = Math.floor(numberChars.length / 2);
    for (var i=offset,j=numberChars.length; i <= midpoint; i++,j--) {
        var temp = numberChars[i];
        numberChars[i] = numberChars[j];
        numberChars[j] = temp;
    }
    var number = Number(numberChars.join(''));
    if (number > MAX_INT32 || number < MIN_INT32) {
        return 0;
    }
    return number;
};