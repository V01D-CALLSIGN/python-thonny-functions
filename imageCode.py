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
            if w>h:
                px[x,y] = (255-r,255-g,255-b)
            if h>w:
                px[x,y] = (255-r,255-g,255-b)
            else:
                px[x,y] = (255-r,255-g,255-b)
    return(img)




#------part 3 functions-----------

# intensify()
# argument: Image 
# returns the Image



# blackWhite()
# argument: Image 
# returns the Image
    



# twoColor()
# arguments: Image, color, color (colors are triplets) 
# returns the Image





# fourColor()
# arguments: Image, color, color, color, color (colors are triplets) 
# returns the Image




# lineDrawing()
# argument: Image 
# returns the Image




#------part 4 functions-----------

# plainBorder()
# argument: Image 
# returns the Image




# colorBorder()
# arguments: Image, color (triplet), thickness (int) 
# returns the Image




# fadeVert()
# argument: Image 
# returns the Image




# fadeHoriz()
# argument: Image 
# returns the Image





#------part 5 functions-----------

# mirrorHoriz()
# argument: Image 
# returns the Image



# mirrorVert()
# argument: Image 
# returns the Image




# flipHoriz()
# argument: Image 
# returns a new Image





# flipVert()
# argument: Image 
# returns a new Image





# shrink()
# argument: Image 
# returns a new Image




# enlarge()
# argument: Image 
# returns a new Image





# rotateRight()
# argument: Image 
# returns a new Image




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

picture = Image.open('bear.jpg')

picture = negate(picture)

picture.show()





