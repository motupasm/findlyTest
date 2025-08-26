// ---------------NAVBAR CONTROL---------------------

// const profileIcon = document.getElementById("person-circle");
// const sidebar = document.getElementById("side-navbar");
const navOpen = document.querySelector(".bi-list-nested");
const leftSideBar = document.querySelector(".left-side-navbar");
const navclose = document.querySelector(".bi-x-lg");
const signInclose = document.querySelector(".bi-x-lg");
const sideBarMenu = document.querySelectorAll(".items");

signInclose.addEventListener("click", (e) => {
  sidebar.classList.toggle("close");
});

navOpen.addEventListener("click", (e) => {
  leftSideBar.style.display = "block";
  navOpen.style.display = "none";
});

navclose.addEventListener("click", (e) => {
  leftSideBar.style.display = "none";
  navOpen.style.display = "block";
});

//-------------------HERO SECTION---------------------------

const userOption = document.querySelectorAll(".userOption");

userOption.forEach((option, index) => {
  option.addEventListener("click", () => {
    userOption.forEach((option) => {
      option.style.backgroundColor = "white";
    });
    option.style.backgroundColor = "transparent";
  });
});

