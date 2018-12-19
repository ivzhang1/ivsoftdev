//Ivan Zhang
//SoftDev1 pd7
//K #28: Sequential Progression
//2018-12-18  

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
    return students[rand];
}
