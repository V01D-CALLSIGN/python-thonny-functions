from PIL import Image


#------identify yourself----------
# put your name (first name last name) into a variable called name

name = "Aarush Bagchi"



#------Helper functions-----------
# in this space, put any functions that don't operate on whole images,
# but provide useful functionality for other functions to call
# The handout will suggest some helper functions to write

def brightness(color):
    r,g,b = color
    return (r+g+b)/3

def avgBrightness(img):
    w = img.width
    h=img.height
    px = img.load()
    total = 0
    for y in range(h):
        for x in range(w):
            total += brightness(px[x,y])
    return total // (w*h)





 
#------part 1 functions-----------

# drawPixel()
# argument: Image 
# returns the Image
def drawPixel(img):
    w = img.width
    h = img.height
    px = img.load()
    px[5,5]=(255,0,0)
    return img




# drawHorizLine()
# argument: Image 
# returns the Image

def drawHorizLine(img):
    w = img.width
    h = img.height
    px = img.load()
    middle = h//2
    for x in range(w):
        px[x,middle] = (255,0,0)
        px[x,middle-1] = (255,0,0)
        px[x,middle+1] = (255,0,0)
    return img




# drawVertLine()
# argument: Image 
# returns the Image

def drawVertLine(img):
    w = img.width
    h = img.height
    px = img.load()
    middle = w//2
    for x in range(h):
        px[middle,x] = (0,0,255)
        px[middle-1,x] = (0,0,255)
        px[middle+1,x] = (0,0,255)
    return img



# drawDiagonalLines()
# argument: Image 
# returns the Image

def drawDiagonalLines(img):
    w = img.width
    h = img.height
    px = img.load()
    yellow = (255, 255, 0)
    for x in range(min(w,h)):
        px[x,x] = yellow
        px[w-1-x,x] = yellow
        
        if x>0:
            px[x, x-1] = yellow
            px[w-1-x, x-1] = yellow
        if x<h-1:
            px[x, x+1] = yellow
            px[w-1-x, x+1] = yellow
    return img

    



    
    
    




#------part 2 functions-----------

# fillRed()
# argument: Image 
# returns the Image

def fillRed(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            if w>h:
                px[x,y] = (255,0,0)
            if h>w:
                px[x,y] = (255,0,0)
            else:
                px[x,y] = (255,0,0)
    return(img)



# fillColor()
# arguments: Image, color (triplet) 
# returns the Image


def fillColor(img,color):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            if w>h:
                px[x,y] = color
            if h>w:
                px[x,y] = color
            else:
                px[x,y] = color
    return(img)
    


# removeRed()
# argument: Image 
# returns the Image

def removeRed(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if w>h:
                px[x,y] = (0,g,b)
            if h>w:
                px[x,y] = (0,g,b)
            else:
                px[x,y] = (0,g,b)
    return(img)


# removeGreen()
# argument: Image 
# returns the Image

def removeGreen(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if w>h:
                px[x,y] = (r,0,b)
            if h>w:
                px[x,y] = (r,0,b)
            else:
                px[x,y] = (r,0,b)
    return(img)




# removeBlue()
# argument: Image 
# returns the Image

def removeBlue(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if w>h:
                px[x,y] = (r,g,0)
            if h>w:
                px[x,y] = (r,g,0)
            else:
                px[x,y] = (r,g,0)
    return(img)




# lighten()
# argument: Image 
# returns the Image
def lighten(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if w>h:
                px[x,y] = (r+50,g+50,b+50)
            if h>w:
                px[x,y] = (r+50,g+50,b+50)
            else:
                px[x,y] = (r+50,g+50,b+50)
    return(img)




# darken()
# argument: Image 
# returns the Image

def darken(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if w>h:
                px[x,y] = (r-50,g-50,b-50)
            if h>w:
                px[x,y] = (r-50,g-50,b-50)
            else:
                px[x,y] = (r-50,g-50,b-50)
    return(img)



# grayscale()
# argument: Image 
# returns the Image

def grayscale(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            gray = int(brightness(px[x,y]))
            if w>h:
                px[x,y] = (gray,gray,gray)
            if h>w:
                px[x,y] = (gray,gray,gray)
            else:
                px[x,y] = (gray,gray,gray)
    return(img)
    


# negate()
# argument: Image 
# returns the Image

def negate(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            px[x,y] = (255-r,255-g,255-b)
    return(img)




#------part 3 functions-----------

# intensify()
# argument: Image 
# returns the Image

def intensify(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            r,g,b = px[x,y]
            if r>= 128:
                r = 255
            else:
                r=0
            if g>=128:
                g = 255
            else:
                g=0
            if b>=128:
                b= 255
            else:
                b=0
            px[x,y] = (r,g,b)
                    
    return(img)
    

# blackWhite()
# argument: Image 
# returns the Image

def blackWhite(img):
    w = img.width
    h = img.height
    px = img.load()
    cutoff = avgBrightness(img)
    for y in range(h):
        for x in range(w):
            b = brightness(px[x,y])
            if b>=cutoff:
                px[x,y] = (255,255,255)
            else:
                px[x,y] = (0,0,0)
    return(img)



# twoColor()
# arguments: Image, color, color (colors are triplets) 
# returns the Image

def twoColor(img, color1,color2):
    w = img.width
    h = img.height
    px = img.load()
    cutoff = avgBrightness(img)
    for y in range(h):
        for x in range(w):
            b = brightness(px[x,y])
            if b>=cutoff:
                px[x,y] = color2
            else:
                px[x,y] = color1
    return(img)




# fourColor()
# arguments: Image, color, color, color, color (colors are triplets) 
# returns the Image

def fourColor(img, color1,color2,color3,color4):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            b = brightness(px[x,y])
            if b<64:
                px[x,y] = color1
            elif b<128:
                px[x,y] = color2
            elif b<192:
                px[x,y] = color3
            else:
                px[x,y] = color4
    return(img)


# lineDrawing()
# argument: Image 
# returns the Image

def lineDrawing(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w-1):
            b1 = brightness(px[x,y])
            b2 = brightness(px[x+1,y])
            if abs(b1-b2)>2:
                px[x,y] = (0,0,0)
            else:
                px[x,y] = (255,255,255)
    return img


#------part 4 functions-----------

# plainBorder()
# argument: Image 
# returns the Image

def plainBorder(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(10):
        for x in range(w):
            px[x, y] = (0, 0, 0)
    for y in range(h - 10, h):
        for x in range(w):
            px[x, y] = (0, 0, 0)
    for y in range(h):
        for x in range(10):
            px[x, y] = (0, 0, 0)
    for y in range(h):
        for x in range(w - 10, w):
            px[x, y] = (0, 0, 0)
    return img


# colorBorder()
# arguments: Image, color (triplet), thickness (int) 
# returns the Image

def colorBorder(img,color,thickness):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(thickness):
        for x in range(w):
            px[x, y] = color
    for y in range(h - thickness, h):
        for x in range(w):
            px[x, y] = color
    for y in range(h):
        for x in range(thickness):
            px[x, y] = color
    for y in range(h):
        for x in range(w - thickness, w):
            px[x, y] = color
    return img


# fadeVert()
# argument: Image 
# returns the Image

def fadeVert(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        percentage = y/(h-1)
        for x in range(w):
            r,g,b = px[x,y]
            px[x,y] =(int(r * percentage), int(g * percentage), int(b * percentage))
    return img




# fadeHoriz()
# argument: Image 
# returns the Image
def fadeHoriz(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w):
            percentage = x/(w-1)
            r,g,b = px[x,y]
            px[x,y] =(int(r * percentage), int(g * percentage), int(b * percentage))
    return img




#------part 5 functions-----------

# mirrorHoriz()
# argument: Image 
# returns the Image

def mirrorHoriz(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h):
        for x in range(w//2):
            px[w-1-x,y] = px[x,y]
    return img


# mirrorVert()
# argument: Image 
# returns the Image
def mirrorHoriz(img):
    w = img.width
    h = img.height
    px = img.load()
    for y in range(h//2):
        for x in range(w):
            px[x,h-1-y] = px[x,y]
    return img



# flipHoriz()
# argument: Image 
# returns a new Image
def flipHoriz(img):
    w = img.width
    h = img.height
    px = img.load()
    newImg = Image.new("RGB", (w, h))
    newPx = newImg.load()
    for y in range(h):
        for x in range(w):
            newPx[w - 1 - x, y] = px[x, y]
    return newImg





# flipVert()
# argument: Image 
# returns a new Image

def flipVert(img):
    w = img.width
    h = img.height
    px = img.load()
    newImg = Image.new("RGB", (w, h))
    newPx = newImg.load()
    for y in range(h):
        for x in range(w):
            newPx[x, h - 1 - y] = px[x, y]
    return newImg





# shrink()
# argument: Image 
# returns a new Image

def shrink(img):
    w = img.width
    h = img.height
    px = img.load()
    newImg = Image.new("RGB", (w // 2, h // 2))
    newPx = newImg.load()
    for y in range(h // 2):
        for x in range(w // 2):
            newPx[x, y] = px[x * 2, y * 2]  
    return newImg



# enlarge()
# argument: Image 
# returns a new Image
def enlarge(img):
    w = img.width
    h = img.height
    px = img.load()
    newImg = Image.new("RGB", (w * 2, h * 2))
    newPx = newImg.load()
    for y in range(h):
        for x in range(w):
            newPx[x * 2,     y * 2]     = px[x, y]
            newPx[x * 2 + 1, y * 2]     = px[x, y]
            newPx[x * 2,     y * 2 + 1] = px[x, y]
            newPx[x * 2 + 1, y * 2 + 1] = px[x, y]
    return newImg




# rotateRight()
# argument: Image 
# returns a new Image
def rotateRight(img):
    w = img.width
    h = img.height
    px = img.load()
    newImg = Image.new("RGB", (h, w))  # width/height are swapped!
    newPx = newImg.load()
    for y in range(h):
        for x in range(w):
            newPx[h - 1 - y, x] = px[x, y]
    return newImg




#------part 6 functions-----------

# blend()
# arguments: Image, Image
# returns a new Image




# paste()
# arguments: Image (foreground), Image (background), int, int
#            (start with just the two images, and add the ints after the function is working)
# returns the background Image





# greenScreen()
# arguments: Image (foreground), Image (background), int, int 
#            (start with just the two images, and add the ints after the function is working)
# returns the background Image





# popArt()
# argument: Image 
# returns a new Image




# -- only function definitions above this line ----
#----------test your functions below -----

picture = Image.open('neptune.jpg')

picture = blackWhite(picture)

picture.show()





