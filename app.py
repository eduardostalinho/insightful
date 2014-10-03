# -*- coding: utf-8 -*-

from flask import Flask, render_template

insightful = Flask('Insightful')

@insightful.route('/')
def hello():
    return render_template('home.html')

@insightful.route('/search/')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    insightful.run(debug=True)
