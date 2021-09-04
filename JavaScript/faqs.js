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