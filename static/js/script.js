function addEducation() {
    // Clone the education section and append it
    var educationSection = document.querySelector('.education-section');
    var clone = educationSection.cloneNode(true);
    educationSection.parentNode.appendChild(clone);
}

function addWorkExperience() {
    // Clone the work experience section and append it
    var workExperienceSection = document.querySelector('.work-experience-section');
    var clone = workExperienceSection.cloneNode(true);
    workExperienceSection.parentNode.appendChild(clone);
}

function addCertification() {
    // Clone the certifications section and append it
    var certificationsSection = document.querySelector('.certifications-section');
    var clone = certificationsSection.cloneNode(true);
    certificationsSection.parentNode.appendChild(clone);
}

function addProject() {
    // Clone the projects section and append it
    var projectsSection = document.querySelector('.projects-section');
    var clone = projectsSection.cloneNode(true);
    projectsSection.parentNode.appendChild(clone);
}