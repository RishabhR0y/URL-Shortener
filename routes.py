from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Link

shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    return ""

@shortener.route('/create_link', methods=['POST'])
def create_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_success.html',
     new_url=link.short_url, original_url=link.original_url)

@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('?analytics')
def analytics():
    return ""

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found</h1>',404


