from PIL import Image 
from numpy import complex, array 
import colorsys
import math
WIDTH = 4096
def rgb_conv(i): 
    color = 255 * array(colorsys.hsv_to_rgb(1.0, i / 255.0, i / 255.0)) 
    return tuple(color.astype(int)) 
def mbrot(x, y): 
    c0 = complex(x, y) 
    c = 0
    for i in range(1, 1000): 
        if abs(c) > 2: 
            return rgb_conv(i) 
        c = c * c + c0 
    return (0, 0, 0) 
img = Image.new('RGB', (WIDTH, int(WIDTH / 2))) 
pixels = img.load()   
for x in range(img.size[0]): 
    print("","%.2f %%" % (x / WIDTH * 100.0),"█"*math.ceil(x / WIDTH * 25.0) + "▒"*(25-math.ceil(x / WIDTH * 25.0)),end="\r")  
    for y in range(img.size[1]): 
        pixels[x, y] = mbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), 
                                      (y - (WIDTH / 4)) / (WIDTH / 4)) 
img.save("fractal.bmp")
