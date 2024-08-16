from flask import render_template, request, jsonify

from app import app


@app.route('/')
def index():
    return render_template('cv_template.html')


@app.route('/update_cv', methods=['POST'])
def update_cv():

    print("update cv")
    return jsonify({'message': 'CV updated and PDF generated!'}), 200
