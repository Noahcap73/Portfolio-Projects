const dropdownBtn = document.getElementById("dropmenubtn");
const dropdownMenu = document.getElementById("dropdownmenu");
const menuIcon = document.getElementById("menu-icon");
const menuIconX = document.getElementById("menu-icon-x");

//Making the drop down menu on mobile visible
const toggleDropDownMenu = () => {
  dropdownMenu.style.visibility = "visible";
};

//Making the menu icon switch
const menuIconTransition = () => {
  // Toggle the rotation class
  if (menuIcon.classList.contains("rotate-90")) {
    menuIcon.classList.remove("rotate-90");
  } else {
    menuIcon.classList.add("rotate-90");
  }

  // Toggle the icon class between "fa-bars" and "fa-times"
  menuIcon.classList.toggle("fa-bars");
  menuIcon.classList.toggle("fa-times");

  dropdownMenu.classList.toggle("hidden");
};

dropdownBtn.addEventListener("click", function (e) {
  e.stopPropagation();
  toggleDropDownMenu();
  menuIconTransition();
});
