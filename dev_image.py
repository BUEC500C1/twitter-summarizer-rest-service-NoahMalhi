from PIL import Image, ImageDraw, ImageFont
import os
import ffmpeg
import threading

def dev_video(username, success):
    #each process runs ffmpeg using its own username.png files
    if (success == 1): 
        pid = os.getpid()
        os.system('ffmpeg -framerate 0.33 -i '+username+'%d.png vid_dir/video'+str(pid)+'.avi')
    else:
        return

def thread_func(tweet_texts, imagelist, username):
    font = ImageFont.truetype("Verdana.ttf" ,12)
    iter = 0
    img_iter = 0
    for (x,y) in tweet_texts:
        
        filename = username + str(iter) + ".png"
        f = open(filename, "w+")
        image = Image.new(mode = "RGB", size = (850,300), color = "red")
        draw = ImageDraw.Draw(image)
        draw.text((20,20), x , fill=(200,200,0), font=font)
        image.save(filename)
        if(y == 1):
            new_name = username + str(iter) + ".png"                      
            im = Image.open(imagelist[img_iter])
            im.save(new_name)
            img_iter += 1
    
        iter +=1
        filename = ''
        f.close()
    

def convert_text(tweet_texts, imagelist, username):
   

    #uses 2 threads to run the conversion of images
    threads = []
    for n in range (1,3):
        x = threading.Thread(target=thread_func, args=(tweet_texts,imagelist,username,))
        x.start()
        threads.append(x)

    for x in threads:
        x.join()
    
  
        
