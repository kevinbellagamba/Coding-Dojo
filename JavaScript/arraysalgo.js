var testArr = [6,3,5,1,2,4];

var sum = 0;
for(var n = 0; n < testArr.length; n++){
    sum += testArr[n];
    console.log("Num: " +testArr[n]+ ", Sum: " +sum);

}

for(var n = 0; n < testArr.length; n++){
    testArr[n] = testArr[n] * n;
}
console.log(testArr);
