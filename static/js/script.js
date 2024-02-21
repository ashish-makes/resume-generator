const mobIcon = document.querySelector(".mob-menu-icon");
const mobCloseIcon = document.querySelector(".mob-menu-close-icon");
const mobMenu = document.querySelector(".mob-menu");
const body = document.querySelector("body");

function toggleMenu() {
    // Check if the menu is already open
    const menuOpen = mobMenu.classList.contains("show-menu");

    // Toggle the visibility of menu icon and close icon
    mobIcon.style.display = menuOpen ? "block" : "none";
    mobCloseIcon.style.display = menuOpen ? "none" : "block";

    // Toggle class to show/hide the mobile menu
    mobMenu.classList.toggle("show-menu");

    // Toggle overflow hidden on the body
    if (mobMenu.classList.contains("show-menu")) {
        body.style.overflow = "hidden"; // Disable scrolling
    } else {
        body.style.overflow = "auto"; // Enable scrolling
    }
}

mobIcon.addEventListener("click", toggleMenu);
mobCloseIcon.addEventListener("click", toggleMenu);