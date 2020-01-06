from flask import render_template,request,redirect,url_for 
from .import main
from .. request import get_source,get_articles
from ..model import Source

@main.route('/')
def index():
    general_news =get_source('general')
    print('*************general news*********************')
    print('general_news')
    
    title='Latest News'
    
    return render_template('index.html,title = title,general=general_news')

@main.route('/article/<int:id>')

def article(id):
    article =get_articles(id)
    print('*************get_article****************')
    print(article)
    
    title = 'Article_Hub'
    
    return render_template(article.html, title = title, id=id, article= article)