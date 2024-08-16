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
    jobs = request.args.get('jobs', 'Default Jobs')

    # Split jobs into a list if needed
    job_list = jobs.split('\n') if jobs else []

    return render_template('cv_template.html', name=name, job_title=job_title, location=location,
                           phone=phone, email=email, linkedin=linkedin, profile_summary=profile_summary,
                           job_list=job_list)
