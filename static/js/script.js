window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar_top");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
    document.getElementById("main").style.marginTop ="60px"
    
  } else {
    navbar.classList.remove("sticky");
  }
}



const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// function login(){
// 	window.alert("Working");
// }