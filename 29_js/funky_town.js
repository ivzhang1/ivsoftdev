//Hi: Ivan Zhang and Jerry Ye
//SoftDev1 pd7
//K#29: Sequential Progression
//2018-12-19


var fibby = function (num){
    if(num == 0){
	return 0;
    }
    if(num < 3){
	return 1;
    }
    return fibby(num - 1) + fibby(num - 2);
}

var gcd = function (a, b){
    if(b == 0){
	return a;
    }
    return gcd(b, a % b);
}

var students = ["Sam", "Tom", "Bobby", "Smith"];


var randomStudent = function (){
    var rand = Math.floor(Math.random() * 4);
    console.log(students[rand]);
    return students[rand];
}

var fib = document.getElementById('fib');
var gcD = document.getElementById('gcd');
var randS = document.getElementById('randomStudent');

var printStudent = function() {
  var stu = randomStudent();
  console.log(stu);
}
var printgcd = function (){
  var num = gcd(5,10);
  console.log(num);
}
var printFib = function (){
  var num = fibby(5);
  console.log(num);
}

fib.addEventListener('click', printFib);
gcD.addEventListener('click', printgcd);
randS.addEventListener('click', printStudent);
