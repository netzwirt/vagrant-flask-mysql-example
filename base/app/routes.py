# -*- coding: utf-8 -*-

from flask import render_template, redirect
import os
from app import app
from app.forms import CommentForm


@app.route("/")
def index():
    
    return render_template('index.html', content='<h1>Welcome to your flask app</h1>')


@app.route("/comment", methods=['GET', 'POST'])
def comment():
    
    form = CommentForm()
    if form.validate_on_submit():
        return redirect('/messages')
        
    return render_template('forms/comment.html', action='/comment', form=form)


@app.route("/messages")
def messages():
    
    return render_template('config.html', config=app.config.items(),configclass=os.environ['APP_SETTINGS'] )
        


@app.route("/config")
def config():
    
    return render_template('config.html', config=app.config.items(),configclass=os.environ['APP_SETTINGS'] )



if __name__ == "__main__":
    app.run(host='0.0.0.0')

