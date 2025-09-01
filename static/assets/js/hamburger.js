const hamburger = document.getElementById("hamburger");
const navMenu = document.querySelector("nav ul"); // ajusta se teu menu for outro seletor

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
});