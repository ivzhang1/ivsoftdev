// Hi: Jerry Ye and Ivan Zhang
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

var addElement = function() {
  var list = document.getElementById("thelist");
  var newElement = document.createElement("li");
  newElement.innerHTML = "new element";
  list.appendChild(newElement);
}
var button = document.getElementById('b');
button.addEventListener('click',addElement)

var list = document.getElementById('thelist');
list.addEventListener('mouseout',function(e){
  document.getElementById('h').innerHTML = 'Hello World!';
});
list.addEventListener('mouseover',function(e){
  document.getElementById('h').innerHTML = e.target.innerHTML;
});
list.addEventListener('click',function(e){
  e.target.remove();
});
var fibonacci = function(n) {
  if(n < 2) {
    return n; // base case
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2); // recursive case
  }
}
var countFib = 0;
var addFib = function() {
  countFib += 1;
  var list = document.getElementById("fiblist");
  var newNumber = document.createElement("li");
  newNumber.innerHTML = fibonacci(countFib);
  list.appendChild(newNumber);
}

var fib = document.getElementById('fb');
fib.addEventListener("click", addFib);
