import twitter_fetch
import dev_image
import threading
from multiprocessing import Process
import os
import sys

#dev_image file contains all functions for making images and videos
#twitter_fetch file is used for getting tweets and images from twitter

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

    return (tweet_texts, image_list)

    


#makes multiple videos at once using multiprocessing
#using Intel i7 with 8 cores and can make 7 videos at once (7 processes)
#gets input from argv --> when running include usernames seperated by spaces
processes = []

if (len(sys.argv) < 2):
    print("Enter a username")
    exit


if (len(sys.argv) < 8):
    for m in range (1,len(sys.argv)):
        username = sys.argv[m]   
        p = Process(target=main, args=(username,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
else:
    print("Can not run with more than 7 usernames/processes")

    