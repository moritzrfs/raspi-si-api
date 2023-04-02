const upButton = document.getElementById("up");
const leftButton = document.getElementById("left");
const downButton = document.getElementById("down");
const rightButton = document.getElementById("right");

upButton.addEventListener("click", function() {
    fetch("http://localhost:8080/start/")
    .then(response => response.json())
    .then(data => console.log(data));
});

leftButton.addEventListener("click", function() {
  alert("Left arrow key clicked!");
});

downButton.addEventListener("click", function() {
  alert("Down arrow key clicked!");
});

rightButton.addEventListener("click", function() {
  alert("Right arrow key clicked!");
});