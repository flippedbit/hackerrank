var myButton = document.createElement('button');
myButton.id = "btn";
myButton.innerHTML = "0";
document.body.appendChild(myButton);
myButton.onclick = function() {
    myButton.innerHTML++;
}