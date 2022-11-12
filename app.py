from celery import Celery
from flask import Flask, request
from pytube import YouTube

app=Flask(__name__)
simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.route('/')
def home_page(): 
    """Just a home page"""
    return "Your app is working!"


@app.route('/simple_start_task')
def call_method():
    """ - This function is asynchoronus method. 
        - This function will call the annother function in the backend to run the celery worker.
        - This function output the ID which will be used to get the information about the task."""        
    app.logger.info("Invoking Method")

    # args from user
    link = request.args.get('link')
    email = request.args.get('email')
    unique_id = request.args.get('unique_id')

    app.logger.info(f"Got all the three request. Link: {link}, Email: {email}, unique_id: {unique_id}.")
    
    if 'amazonaws' in link: 
        yt_title = link.split('/')[-1].replace('%', '_')

    else: 
        yt_obj = YouTube(link)
        yt_title = yt_obj.title  

    r = simple_app.send_task('tasks.predict', kwargs={'link': link, 'email': email, 'youtube_title': yt_title, 'unique_id':unique_id })
    app.logger.info(r.backend)

    return r.id

