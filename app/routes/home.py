from flask import Blueprint, render_template

#blueprint consolidates routes into a single bp object, add @bp.route('/') decorator to turn it into a route
#render template allows us to call upon one of the templates we have to be returned to client

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
def single(id): #captures id from the route
  return render_template('single-post.html')