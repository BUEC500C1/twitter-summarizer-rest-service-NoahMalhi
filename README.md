# Video Encoder FFMPEG
## Noah Malhi

For this hw, I utilized the twitter api. The format of the video is the image and then the tweet in which the image came from.

My assignment is able to run about 5 processes. At that point the terminal I am running is buggy after the run. To view the running processes, in my bash script:
    restart.sh
I used the command line cmd: ps -ef | grep python
This finds all the running processes produces from python. 

The processes of converted text to images was threaded. From using the linux 'time' command' I was able to lower run time by about .2 in most cases for total run time.

For multiprocessing I used "Processes" imported from multiprocessors. I was at most able to execute 6 processes cleanly. I made a lists of processes and had a four loop to call the main 6 times. The made processes were added to the list and after all the processes were made thier was a proccess join to wait for all the proccesses to complete before the program ended.

The separate videos were saved as video(process number).avi. Each process number was attained by using getpid().

Usernames can be changed in the restart.sh scrip. 

The syntax for running the program without the script is:
python3 main.py username1 username2 username3 username4 etc

The number of processes can change dynamically based on number of inputted usernames. Anything above 5 usernames would slow down the system significantly and break the terminal so it is error checked.

The following are some images from the video:
