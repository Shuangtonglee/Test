from flask import render_template,request
from . import mod
from .forms import PastebinEntry

@mod.route('/homepage')
def homepage():
    name = request.endpoint
    form = PastebinEntry()
    return render_template('site/site.html',name = name,form = form)