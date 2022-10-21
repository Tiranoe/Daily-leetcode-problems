// Leetcode problem 9. Palindrome Number
/* Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
*/
/*
function Palindrome(x) {
    // return x === x.split('').reverse().join('');
    for(let i = 0; i < x.length / 2; i++){
        if (x[i] !== x[x.length - 1 - i])
        return false;
    }
    return true;
}

console.log(Palindrome(123))
console.log(Palindrome(121))
*/

//If we want to use the convert the x into strings - I found this simple method

function Palin(x) {
    return (x.toString() == x.toString().split("").reverse().join(""))
}

console.log(Palin(123)) // false
console.log(Palin(123454321)) // True
