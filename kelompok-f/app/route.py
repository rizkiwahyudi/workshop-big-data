from flask import Blueprint, render_template

router = Blueprint('route', __name__, template_folder='template')

@router.route('/')
def index():
    return render_template('index.html')
