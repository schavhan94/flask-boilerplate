from flask import Blueprint, render_template, url_for
from .models import *
from ..app import db

home_blueprint = Blueprint('home',__name__,template_folder='templates')


@home_blueprint.route('/')
def home():
    return render_template('home/home.html', title='Home')