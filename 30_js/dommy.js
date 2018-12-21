// Hi: Jerry Ye and Ivan Zhang
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-20

var addElement = function() {
    var list = document.getElementById("thelist"); // gets unordered list HTML element
    var newElement = document.createElement("li"); // Creates a new list item
    newElement.innerHTML = "new element"; // Gives the new list item text 'new element'
    list.appendChild(newElement); // Adds element to list
}

var button = document.getElementById('b');
button.addEventListener('click',addElement); // Adds 'addElement' capibilities to the button

var list = document.getElementById('thelist');
list.addEventListener('mouseout',function(e){
    document.getElementById('h').innerHTML = 'Hello World!'; // Adds text 'Hello World' to the heading
});
list.addEventListener('mouseover',function(e){
    document.getElementById('h').innerHTML = e.target.innerHTML; // Adds custom text to heading based on list item text
});
list.addEventListener('click',function(e){
    e.target.remove(); // Removes list item based on clicks
});

var flist = [0,1]; / Dynamic programmmmmmmiinnnnggg!
var fibonacci = function(n) {

    if(n < flist.length) {
	return flist[n]; // base case
    }
    else {
	flist[n] = fibonacci(n-1) + fibonacci(n-2); // recursive case
	return flist[n];
    }
}
var countFib = 0;
var addFib = function() {
    countFib += 1; // Adds one to countFib based on clicks
    var list = document.getElementById("fiblist");
    var newNumber = document.createElement("li");
    newNumber.innerHTML = fibonacci(countFib); // Calculates the fib based on countFib
    list.appendChild(newNumber); // adds number to list
}

var fib = document.getElementById('fb');
fib.addEventListener("click", addFib); // Adds 'addFib' functionality to a button
