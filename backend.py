from flask import Flask, send_file, request, render_template, redirect
from multiprocessing import Process
import threading
from multiprocessing import Process
import os
import dev_image
import twitter_fetch
import zipfile

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
@app.route("/", methods=['POST'])
def render_videos():
    #on submit request usernames from html from user input
    handle1 = request.form['handle1']
    handle2 = request.form['handle2']
    handle3 = request.form['handle3']
    handle4 = request.form['handle4']
    os.system("rm -r *.png")
    os.system("rm -r *.jpg")
    os.system("rm -r vid_dir/*")
    
    nameList = [handle1, handle2, handle3, handle4]
    init_prog(nameList)


    zip_it = zipfile.ZipFile('results.zip','w', zipfile.ZIP_DEFLATED)
    for root, directs, files in os.walk('vid_dir/'):
        for vid in files:
            zip_it.write('vid_dir/' + str(vid))
    zip_it.close()
 
    return send_file('results.zip', mimetype ='zip', attachment_filename = 'results.zip', as_attachment=True)


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

    os.system("rm -r *.png")
    os.system("rm -r *.jpg")
    return (tweet_texts, image_list)


    