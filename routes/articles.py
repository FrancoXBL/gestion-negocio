from flask import Blueprint, render_template

articles = Blueprint('article', __name__)

@articles.route('/articles')
def show_article():
    return render_template('articles/articles.html')

@articles.route('/new-article')
def add_article():
    return render_template('articles/new-article.html')

@articles.route('/edit-article')
def edit_article():
    return render_template('articles/edit-article.html')

@articles.route('/delete-article')
def delete_article():
    return render_template('articles/delete-article.html')