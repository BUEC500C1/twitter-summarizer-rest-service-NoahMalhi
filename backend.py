from flask import Flask, escape, request, render_template, redirect
from multiprocessing import Process
import threading
from multiprocessing import Process
import os
import dev_image
import twitter_fetch

app = Flask(__name__)


if (__name__ == "__main__"):
    app.run(
        host="127.0.0.1",
        port=5000
)

@app.route('/')
def app_call():
    return render_template("main.html")


#redirect to page with the resulting videos
@app.route("/render_video", methods=['POST'])
def render_videos():
    #on submit request usernames from html from user input
    handle1 = request.form['handle1']
    handle2 = request.form['handle2']
    handle3 = request.form['handle3']
    handle4 = request.form['handle4']
    nameList = [handle1, handle2, handle3, handle4]
    init_prog(nameList)

   
    return render_template("data_page.html")

#run up to four proccesses to make videos
def init_prog(usernames):
    processes = []

    for name in usernames:
        if (name != ''):
            p = Process(target=main, args=(name,))
            p.start()
            processes.append(p)
    for p in processes:
        p.join()

def main(username):

    if (username.isdigit()):
        print("Username can not be all numbers")
        return 0

    if (username == ''):
        print("Please enter a username")
        return 0
    
    image_list = []
    (image_list, tweet_texts, success) = twitter_fetch.vision_feed(image_list, username)

    dev_image.convert_text(tweet_texts, image_list, username)

    dev_image.dev_video(username, success)

    os.system('rm -r *.png')
    return (tweet_texts, image_list)


    