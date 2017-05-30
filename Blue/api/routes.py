from flask import Blueprint,render_template

mod = Blueprint('api',__name__)

@mod.route('/getStuff')
def getstuff():
    return render_template('api/api.html')