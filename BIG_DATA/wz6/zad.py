# kafelkarz
from PIL import Image

img= Image.open("test.png")
pixels=img.load()
cols,rows=img.size
tSize= 8 # rozmiar pojedynczego kafelka
s=tSize*tSize

for i in range((int)(cols/tSize)):
    for j in range((int)(rows/tSize)):
        r,g,b =(0,0,0)
        for x in range(tSize):
            for y in range(tSize):
                rPx,gPx,bPx=pixels[i*tSize+x,j*tSize+y]
                r+=rPx
                g+=gPx
                b+=bPx
        
        r=(int)(r/s)
        g=(int)(g/s)
        b=(int)(b/s)

        for x in range(tSize):
            for y in range(tSize):
                pixels[i*tSize+x,j*tSize+y]=(r,g,b)

img.save(f"tile_{tSize}.png")


#img.show()
        
