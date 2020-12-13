from PIL import Image
import os
import cv2

dir = 'D:\\Videotomc\\video_data'

imgs = []

for i in range(1,143):
    imgs.append(os.path.join(dir,"image%d.png" % i))


total_width = 0
total_height = 0
max_width = 0
max_height = 0
ix =[]
for img in imgs:
    im = Image.open(img)
    size = im.size
    w = size[0]
    h = size[1]
    total_width += w 
    total_height += h
    
    if h > max_height:
        max_height = h
    if w > max_width:
        max_width = w
    ix.append(im) 
target_vertical = Image.new('RGB', (max_width, total_height))
pre_w = 0
pre_h = 0
for img in ix:
    target_vertical.paste(img, (pre_w, pre_h, pre_w+max_width, pre_h + img.size[1]))
    pre_h += img.size[1]
target_vertical.show()
target_vertical.save(os.path.join(dir,'pigscene.png'), quality=100)
