// trying out the medium level problem

/* You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*/

let addTwoNumbers = function(l1, l2) {
    let number1 = l1.reverse().join("");
    let number2 = l2.reverse().join("");
    console.log(number1)
    console.log(number2)
};

addTwoNumbers([2,4,3], [5,6,4]);