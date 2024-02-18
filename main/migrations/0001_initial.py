# Generated by Django 4.1.4 on 2024-02-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50)),
                ('linkedin', models.URLField(blank=True)),
                ('portfolio', models.URLField(blank=True)),
                ('unique_identifier', models.CharField(max_length=10, unique=True)),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('field_of_study', models.CharField(default='', max_length=100)),
                ('institution', models.CharField(default='', max_length=100)),
                ('institution_location', models.CharField(default='', max_length=100)),
                ('graduation_year', models.IntegerField(blank=True)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('work_location', models.CharField(blank=True, max_length=100)),
                ('employment_dates', models.CharField(blank=True, max_length=100)),
                ('responsibilities', models.TextField(blank=True)),
                ('achievements', models.TextField(blank=True)),
                ('certification_name', models.CharField(blank=True, max_length=100)),
                ('issuing_organization', models.CharField(blank=True, max_length=100)),
                ('date_earned', models.DateField(blank=True)),
                ('project_title', models.CharField(blank=True, max_length=100)),
                ('project_description', models.TextField(blank=True)),
                ('your_role', models.CharField(blank=True, max_length=100)),
                ('technologies_used', models.TextField(blank=True)),
                ('project_url', models.URLField(blank=True)),
                ('technical_skills', models.TextField(blank=True)),
                ('soft_skills', models.TextField(blank=True)),
                ('language_proficiency', models.TextField(blank=True)),
                ('awards_honors', models.TextField(blank=True)),
                ('volunteer_experience', models.TextField(blank=True)),
                ('interests_hobbies', models.TextField(blank=True)),
            ],
        ),
    ]