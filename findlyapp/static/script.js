// ---------------NAVBAR CONTROL---------------------

const profileIcon = document.getElementById("person-circle");
const sidebar = document.getElementById("side-navbar");
const navOpen = document.querySelector(".bi-list-nested");
const leftSideBar = document.querySelector(".left-side-navbar");
const navclose = document.querySelector(".bi-x-lg");
const signInclose = document.querySelector(".bi-x-lg");

profileIcon.addEventListener("click", (e) => {
  sidebar.classList.toggle("hidden");
});

navOpen.addEventListener("click", (e) => {
  leftSideBar.style.display = "block";
  navOpen.style.display = "none";
});
navclose.addEventListener("click", (e) => {
  leftSideBar.style.display = "none";
  navOpen.style.display = "block";
});

// const menuItems = document.querySelectorAll(".button-item-menu");

// menuItems.forEach((menu, index) => {
//   menu.addEventListener("click", () => {
//     menuItems.forEach((menu) => {
//       menu.style.backgroundColor = "transparent";
//     });
//     menu.style.backgroundColor = "#4d6afed9";
//   });
// });
// -------------------HERO SECTION---------------------------

const userOption = document.querySelectorAll(".userOption");

userOption.forEach((option, index) => {
  option.addEventListener("click", () => {
    userOption.forEach((option) => {
      option.style.backgroundColor = "white";
    });
    option.style.backgroundColor = "transparent";
  });
});
