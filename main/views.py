from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect, get_object_or_404
from .models import PersonalInformation

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def builder(request):
    if request.method == 'POST':
        # Generate a random unique identifier
        unique_identifier = get_random_string(length=10)

        # Create PersonalInformation object with all details
        personal_info = PersonalInformation.objects.create(
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            address=request.POST.get('address', ''),
            dob=request.POST.get('dob', None),
            nationality=request.POST.get('nationality', ''),
            linkedin=request.POST.get('linkedin', ''),
            portfolio=request.POST.get('portfolio', ''),
            unique_identifier=unique_identifier,


            # Education
            degree=request.POST.get('degree', ''),
            field_of_study=request.POST.get('field_of_study', ''),
            institution=request.POST.get('institution', ''),
            institution_location=request.POST.get('institution_location', ''),
            graduation_year=request.POST.get('graduation_year', None),
            gpa=request.POST.get('gpa', None),

            degree_1=request.POST.get('degree_1', ''),
            field_of_study_1=request.POST.get('field_of_study_1', ''),
            institution_1=request.POST.get('institution_1', ''),
            institution_location_1=request.POST.get('institution_location_1', ''),
            graduation_year_1=request.POST.get('graduation_year_1', None) or None,
            gpa_1=request.POST.get('gpa_1', None) or None,


            # Work Experience
            job_title=request.POST.get('job_title', ''),
            company=request.POST.get('company', ''),
            work_location=request.POST.get('work_location', ''),
            employment_dates=request.POST.get('employment_dates', ''),
            responsibilities=request.POST.get('responsibilities', ''),

            job_title_1=request.POST.get('job_title_1', ''),
            company_1=request.POST.get('company_1', ''),
            work_location_1=request.POST.get('work_location_1', ''),
            employment_dates_1=request.POST.get('employment_dates_1', ''),
            responsibilities_1=request.POST.get('responsibilities_1', ''),

            job_title_2=request.POST.get('job_title_2', ''),
            company_2=request.POST.get('company_2', ''),
            work_location_2=request.POST.get('work_location_2', ''),
            employment_dates_2=request.POST.get('employment_dates_2', ''),
            responsibilities_2=request.POST.get('responsibilities_2', ''),
            # achievements=request.POST.get('achievements', ''),


            # Certification
            certification_name=request.POST.get('certification_name', ''),
            issuing_organization=request.POST.get('issuing_organization', ''),
            date_earned=request.POST.get('date_earned', None) or None,

            certification_name_1=request.POST.get('certification_name_1', ''),
            issuing_organization_1=request.POST.get('issuing_organization_1', ''),
            date_earned_1=request.POST.get('date_earned_1', None) or None,


            # Project
            project_title=request.POST.get('project_title', ''),
            project_description=request.POST.get('project_description', ''),
            technologies_used=request.POST.get('technologies_used', ''),
            project_url=request.POST.get('project_url', ''),

            project_title_1=request.POST.get('project_title_1', ''),
            project_description_1=request.POST.get('project_description_1', ''),
            technologies_used_1=request.POST.get('technologies_used_1', ''),
            project_url_1=request.POST.get('project_url_1', ''),

            project_title_2=request.POST.get('project_title_2', ''),
            project_description_2=request.POST.get('project_description_2', ''),
            technologies_used_2=request.POST.get('technologies_used_2', ''),
            project_url_2=request.POST.get('project_url_2', ''),
            # Skills
            technical_skills=request.POST.get('technical_skills', ''),
            soft_skills=request.POST.get('soft_skills', ''),
            # language_proficiency=request.POST.get('language_proficiency', ''),
        )

        # Redirect to the resume page with the unique identifier
        return redirect('resume', unique_identifier=unique_identifier)

    return render(request, 'builder.html', {})


def resume(request, unique_identifier):
    personal_info = get_object_or_404(PersonalInformation, unique_identifier=unique_identifier)
    responsibilities_list = personal_info.responsibilities.split('\n')
    responsibilities_list_1 = personal_info.responsibilities_1.split('\n')
    responsibilities_list_2 = personal_info.responsibilities_2.split('\n')
    technical_skills_list = personal_info.technical_skills.split('\n')
    soft_skills_list = personal_info.soft_skills.split('\n')
    return render(request, 'resume.html', {'personal_info': personal_info, 'responsibilities_list': responsibilities_list, 'technical_skills_list': technical_skills_list, 'soft_skills_list': soft_skills_list, 'responsibilities_list_1': responsibilities_list_1, 'responsibilities_list_2': responsibilities_list_2,})

# from django.utils.crypto import get_random_string
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import PersonalInformation
# import json

# def index(request):
#     return render(request, 'index.html', {})

# def about(request):
#     return render(request, 'about.html', {})

# def contact(request):
#     return render(request, 'contact.html', {})

# def builder(request):
#     if request.method == 'POST':
#         # Generate a random unique identifier
#         unique_identifier = get_random_string(length=10)

#         # Convert list fields to JSON
#         educations = []
#         work_experiences = []
#         certifications = []
#         projects = []

#         for i in range(len(request.POST.getlist('degree'))):
#             educations.append({
#                 'degree': request.POST.getlist('degree')[i],
#                 'field_of_study': request.POST.getlist('field_of_study')[i],
#                 'institution': request.POST.getlist('institution')[i],
#                 'institution_location': request.POST.getlist('institution_location')[i],
#                 'graduation_year': request.POST.getlist('graduation_year')[i],
#                 'gpa': request.POST.getlist('gpa')[i]
#             })

#         for i in range(len(request.POST.getlist('job_title'))):
#             work_experiences.append({
#                 'job_title': request.POST.getlist('job_title')[i],
#                 'company': request.POST.getlist('company')[i],
#                 'work_location': request.POST.getlist('work_location')[i],
#                 'employment_dates': request.POST.getlist('employment_dates')[i],
#                 'responsibilities': request.POST.getlist('responsibilities')[i],
#                 'achievements': request.POST.getlist('achievements')[i]
#             })

#         for i in range(len(request.POST.getlist('certification_name'))):
#             certifications.append({
#                 'certification_name': request.POST.getlist('certification_name')[i],
#                 'issuing_organization': request.POST.getlist('issuing_organization')[i],
#                 'date_earned': request.POST.getlist('date_earned')[i]
#             })

#         for i in range(len(request.POST.getlist('project_title'))):
#             projects.append({
#                 'project_title': request.POST.getlist('project_title')[i],
#                 'project_description': request.POST.getlist('project_description')[i],
#                 'your_role': request.POST.getlist('your_role')[i],
#                 'technologies_used': request.POST.getlist('technologies_used')[i],
#                 'project_url': request.POST.getlist('project_url')[i]
#             })

#         # Create PersonalInformation object with all details
#         personal_info = PersonalInformation.objects.create(
#             full_name=request.POST.get('full_name'),
#             phone=request.POST.get('phone'),
#             email=request.POST.get('email'),
#             address=request.POST.get('address', ''),
#             dob=request.POST.get('dob', None),
#             nationality=request.POST.get('nationality', ''),
#             linkedin=request.POST.get('linkedin', ''),
#             portfolio=request.POST.get('portfolio', ''),
#             unique_identifier=unique_identifier,
#             educations=json.dumps(educations),
#             work_experiences=json.dumps(work_experiences),
#             certifications=json.dumps(certifications),
#             projects=json.dumps(projects),
#             technical_skills=request.POST.get('technical_skills', ''),
#             soft_skills=request.POST.get('soft_skills', ''),
#             language_proficiency=request.POST.get('language_proficiency', ''),
#             awards_honors=request.POST.get('awards_honors', ''),
#             volunteer_experience=request.POST.get('volunteer_experience', ''),
#             interests_hobbies=request.POST.get('interests_hobbies', '')
#         )

#         # Redirect to the resume page with the unique identifier
#         return redirect('resume', unique_identifier=unique_identifier)

#     return render(request, 'builder.html', {})


# def resume(request, unique_identifier):
#     personal_info = get_object_or_404(PersonalInformation, unique_identifier=unique_identifier)
#     educations = json.loads(personal_info.educations)
#     work_experiences = json.loads(personal_info.work_experiences)
#     certifications = json.loads(personal_info.certifications)
#     projects = json.loads(personal_info.projects)
#     return render(request, 'resume.html', {'personal_info': personal_info, 'educations': educations, 'work_experiences': work_experiences, 'certifications': certifications, 'projects': projects})