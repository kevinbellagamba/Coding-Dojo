// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.
function buildArr(){
    var arr = [];
    for(var i = 1; i <=255; i++){
        arr.push(i);
    }
    return arr;
}
var result = buildArr();
console.log(result);

// 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.
function even1000(){
    sum = 0;
    for(var i = 0; i <= 1000; i++){
        if(i % 2 == 0){
        sum = sum + i;
        }
    }
    return sum;
}
console.log(even1000());


// 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).
function odd5000(){
    sum = 0;
    for(var i = 0; i <= 5000; i++){
        if(i % 2 != 0){
            sum = sum + i;
        }
    }
    return sum;
}
console.log(odd5000());


// 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).
function iterateArr(arr){
    sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    return sum;
}
console.log(iterateArr([1,2,3,4,5,3,1,23,9]));



// 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
function findMax(arr){
    var max = arr[0];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        
    }
    return max;
}
console.log(findMax([1,2,3,2,1,21,1,3,2]))



// 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
function findAvg(arr){
    var sum = 0;
    var avg = 0;
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    avg = sum / arr.length;
    return avg;
}
console.log(findAvg([1,2,3,4]));



// 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.
function arrOdd() {
    var newArr = [];
    for(var i = 0; i < 50; i++){
        if(i % 2 != 0)
        newArr.push(i);
    }
    return newArr;
}
console.log(arrOdd());



// 8. Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).
function greaterThanY(arr,y) {
    var counter = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > y){
            counter++;
        }
    }
    return counter;
}
console.log(greaterThanY([1,2,3,4,5,22,13,0,-2], 3))



// 9. Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
function square(arr) {
    for(var i = 0; i < arr.length; i++){
        arr[i] *= arr[i];
    }
    return arr;
}
console.log(square([2,4,16,25]));



// 10. Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
function noNeg(arr) {
    for (var i = 0; i < arr.length; i++){
        if (arr[i] < 0){
            arr[i] = arr[i] * -0;
        }
    }
    return arr;
}
console.log(noNeg([-2,-4,6,8,1,-10,9,-81]));


// 11. Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])
function maxMinAvg(arr) {
    var max = arr[0];
    var min = arr[0];
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
        if(arr[i] > max){
            max = arr[i];
        }
        else if(arr[i] < min){
            min = arr[i];
        }
    }

    var newArr = [];
    newArr.push(max);
    newArr.push(min);
    var avg = sum / arr.length;
    newArr.push(avg);
    return newArr;
}
console.log(maxMinAvg([2,12,4,-2,80,92,6,-54,92]));




// 12. Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).
function swapVals(arr) {
    var temp = arr[0];
    arr[0] = arr[arr.length -1];
    arr[arr.length - 1] = temp; 
    return arr;
}
console.log(swapVals([2,3,4,1,7,-5,7,2,3,4]))


// 13. Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].
function numToString(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0) {
            arr[i] = "Dojo";
        }
    }
    return arr;
}
console.log(numToString([-2,-4,5,6,-7,8]));

var msg = 'codingdojo';
for(var x = 1; x < msg.length - 2; x++)
{
    if(msg.length == 5)
    {
        for(var i = 0; i < 3; i++)
        {
            console.log(i);
        }
    }
    else{
        for(var i = msg.length; i > (msg.length -1); i--)
        {
            console.log(i);
        }
    }
}