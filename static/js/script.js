// var educationCount = 1;
// var workExperienceCount = 1;
// var certificationCount = 1;
// var projectCount = 1;

// function addEducation() {
//     var educationSection = document.querySelector('.education-section');
//     var clone = educationSection.cloneNode(true);
//     updateIds(clone, 'education', educationCount++);
//     var addButton = document.querySelector('button[type="button"][onclick="addEducation()"]');
//     addButton.parentNode.insertBefore(clone, addButton);
// }

// function addWorkExperience() {
//     var workExperienceSection = document.querySelector('.work-experience-section');
//     var clone = workExperienceSection.cloneNode(true);
//     updateIds(clone, 'work-experience', workExperienceCount++);
//     var addButton = document.querySelector('button[type="button"][onclick="addWorkExperience()"]');
//     addButton.parentNode.insertBefore(clone, addButton);
// }

// function addCertification() {
//     var certificationsSection = document.querySelector('.certifications-section');
//     var clone = certificationsSection.cloneNode(true);
//     updateIds(clone, 'certifications', certificationCount++);
//     var addButton = document.querySelector('button[type="button"][onclick="addCertification()"]');
//     addButton.parentNode.insertBefore(clone, addButton);
// }

// function addProject() {
//     var projectsSection = document.querySelector('.projects-section');
//     var clone = projectsSection.cloneNode(true);
//     updateIds(clone, 'projects', projectCount++);
//     var addButton = document.querySelector('button[type="button"][onclick="addProject()"]');
//     addButton.parentNode.insertBefore(clone, addButton);
// }

// function updateIds(clone, sectionType, count) {
//     clone.querySelectorAll('[id]').forEach(function(element) {
//         element.id = element.id + '-' + sectionType + '-' + count;
//     });
// }

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
