from flask import render_template, request
from app import app


@app.route('/')
def index():
    return render_template('cv_template.html')


@app.route('/generate_cv')
def generate_cv():
    # Extract all parameters from the URL
    name = request.args.get('name', 'Default Name')
    job_title = request.args.get('job_title', 'Default Job Title')
    location = request.args.get('location', 'Default Location')
    phone = request.args.get('phone', 'Default Phone')
    email = request.args.get('email', 'Default Email')
    linkedin = request.args.get('linkedin', 'Default LinkedIn')
    profile_summary = request.args.get('profile_summary', 'Default Profile Summary')
    jobs = request.args.get('jobs', '')
    educations = request.args.get('educations', '')
    languages = request.args.get('languages', 'Default Languages')

    # Parse job details
    job_list = []
    if jobs:
        job_entries = jobs.split('||')
        for entry in job_entries:
            parts = entry.split('~')  # Changed to the new delimiter
            if len(parts) == 4:
                job_list.append({
                    'title': parts[0],
                    'start_year': parts[1],
                    'end_year': parts[2],
                    'responsibilities': parts[3].split(',,')
                })

    education_list = []
    if educations:
        education_entries = educations.split('||')
        for entry in education_entries:
            parts = entry.split('~')
            if len(parts) == 3:
                education_list.append({
                    'institution': parts[0],
                    'start_year': parts[1],
                    'end_year': parts[2]
                })

    language_list = []
    if languages:
        language_entries = languages.split(',')
        for language in language_entries:
            language_list.append({
                'language': language
            })

    return render_template('cv_template.html', name=name, job_title=job_title, location=location,
                           phone=phone, email=email, linkedin=linkedin, profile_summary=profile_summary,
                           job_list=job_list, education_list=education_list, language_list=language_list)
