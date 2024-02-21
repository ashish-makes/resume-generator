from django.db import models

class PersonalInformation(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    unique_identifier = models.CharField(max_length=10, unique=True)


    # Education
    degree = models.CharField(max_length=100, blank=True)
    field_of_study = models.CharField(max_length=100, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    institution_location = models.CharField(max_length=100, blank=True)
    graduation_year = models.IntegerField(default=0)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    degree_1 = models.CharField(max_length=100, blank=True)
    field_of_study_1 = models.CharField(max_length=100, blank=True)
    institution_1 = models.CharField(max_length=100, blank=True)
    institution_location_1 = models.CharField(max_length=100, blank=True)
    graduation_year_1 = models.IntegerField(default=0)
    gpa_1 = models.DecimalField(max_digits=4, decimal_places=2, default=0)


    # Work Experience
    job_title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    work_location = models.CharField(max_length=100, blank=True)
    employment_dates = models.CharField(max_length=100, blank=True)
    responsibilities = models.TextField(blank=True)

    job_title_1 = models.CharField(max_length=100, blank=True)
    company_1 = models.CharField(max_length=100, blank=True)
    work_location_1 = models.CharField(max_length=100, blank=True)
    employment_dates_1 = models.CharField(max_length=100, blank=True)
    responsibilities_1 = models.TextField(blank=True)

    job_title_2 = models.CharField(max_length=100, blank=True)
    company_2 = models.CharField(max_length=100, blank=True)
    work_location_2 = models.CharField(max_length=100, blank=True)
    employment_dates_2 = models.CharField(max_length=100, blank=True)
    responsibilities_2 = models.TextField(blank=True)
    # achievements = models.TextField(blank=True)

    # Certification
    certification_name = models.CharField(max_length=100, blank=True)
    issuing_organization = models.CharField(max_length=100, blank=True)
    date_earned = models.DateField(blank=True, null=True)

    certification_name_1 = models.CharField(max_length=100, blank=True)
    issuing_organization_1 = models.CharField(max_length=100, blank=True)
    date_earned_1 = models.DateField(blank=True, null=True)

    # Project
    project_title = models.CharField(max_length=100, blank=True)
    project_description = models.TextField(blank=True)
    technologies_used = models.TextField(blank=True)
    project_url = models.URLField(blank=True)
    
    project_title_1 = models.CharField(max_length=100, blank=True)
    project_description_1 = models.TextField(blank=True)
    technologies_used_1 = models.TextField(blank=True)
    project_url_1 = models.URLField(blank=True)

    project_title_2 = models.CharField(max_length=100, blank=True)
    project_description_2 = models.TextField(blank=True)
    technologies_used_2 = models.TextField(blank=True)
    project_url_2 = models.URLField(blank=True)

    # Skills
    technical_skills = models.TextField(blank=True)
    soft_skills = models.TextField(blank=True)
    # language_proficiency = models.TextField(blank=True)
