from PIL import Image
import os
import cv2
import sys

def TurnVideoIntoImageSequence(videoName, dir): #Turn Video into Images with openCV
    cap = cv2.VideoCapture(os.path.join(dir,videoName))
    success,image = cap.read()

    frameFrequency=1

    #iterate all frames
    total_frame = 0
    count = 0
    
    while True:
        ret, frame = cap.read()
        if ret == False:
            print("Done")
            break
        total_frame += 1
        if total_frame%frameFrequency == 0:
            count += 1
            image_name = os.path.join(dir, videoName2 + "%d.png" % count)
            cv2.imwrite(image_name, frame)
    return count



def StackImages(videoName, dir, TotalFrames): #Stack the images vertically using Pillow
    imgs = []

    for i in range(1,TotalFrames):
        imgs.append(os.path.join(dir,videoName2+"%d.png" % i))

    tw = 0
    th = 0
    mw = 0
    mh = 0
    ix =[]
    for img in imgs:
        im = Image.open(img)
        size = im.size
        w = size[0]
        h = size[1]
        tw += w 
        th += h
        
        if h > mh:
            mh = h
        if w > mw:
            mw = w
        ix.append(im) 
    target_vertical = Image.new('RGB', (mw, th))
    pre_w = 0
    pre_h = 0
    for img in ix:
        target_vertical.paste(img, (pre_w, pre_h, pre_w+mw, pre_h + img.size[1]))
        pre_h += img.size[1]
    #target_vertical.show() #Un-comment this for the image to be opened when done.
    target_vertical.save(os.path.join(dir,'V_image.png'), quality=100)
    print("Done")

if __name__ == "__main__":
    if str(sys.argv[1]) == "none": #Use Output Path as Current script path if no path is given
        dir = str(sys.argv[0])
        dir = dir[:len(dir)-13] #Remove Script Name From Path
    else:
        dir = str(sys.argv[1]) # If Given Get Output Path 
    
    videoName = sys.argv[2] # Initalize video name variable
    videoName2 = ''
    for i in str(sys.argv[2]): # Only get the name not the file extension
        if i == '.':
            break
        videoName2 += i

    TotalFrames = TurnVideoIntoImageSequence(videoName, dir)
    StackImages(videoName2, dir, TotalFrames)

