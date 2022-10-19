// Leetcode problem 9. Palindrome Number

/* Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
*/

function Palindrome(x) {
    // return x === x.split('').reverse().join('');
    for(let i = 0; i < x.length / 2; i++){
        if (x[i] !== x[x.length - 1 - i])
        return false;
    }
    return true;
}

console.log(Palindrome(123))