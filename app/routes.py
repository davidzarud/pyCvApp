from flask import render_template, request, jsonify

from app import app


@app.route('/')
def index():
    return render_template('cv_template.html')


@app.route('/generate_cv')
def generate_cv():
    name = request.args.get('name', 'Default Name')
    return render_template('cv_template.html', name=name)
