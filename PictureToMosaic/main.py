
import os, os.path
from PIL import Image, ImageStat

root: str = "PictureToMosaic"
tiles_dir: str = root+"tiles/"
num_tiles: int = len(os.listdir(sourcefolder)) #need to create function to ignore folders, etc
resized_tiles_dir: str = root+"resized_tiles/"
cropped_resized_tiles_dir: str = root+"cropped_resized_tiles/"
greyed_cropped_resized_dir: str = root+"greyed_cropped_resized_tiles/"
master_image_dir:str = root+"master_image/"
master_image_cropped_dir:str = root+"master_image_cropped"

thumbsize: tuple = (10,10)

sourceBrightness:list= []
masterCropBrightness:list = []

#Start of program



print("Source folder contains " + str(num_tiles)+" images") #Show number of sourcefolder images being processed

target = os.path.join(root,"resized_tiles/")#


def makeDir(dir):
    if os.path.exists(dir) == True:
            clearDirectory(dir)
    else:
        os.mkdir(dir)
        print("Directory " + dir + " created successfully")
    

def clearDirectory(dir): #clear directory if files present
   try:
     files = os.listdir(dir)
     for file in files:
       file_path = os.path.join(dir, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files in " + dir + " deleted successfully.")
   except OSError:
     print("Error occurred while deleting files in " + dir)

def resize(source,target):
    
    files = os.listdir(source)
    i: int = 0

    for item in files:
        infile = os.path.join(source,item)
        im = Image.open(infile)
        w,h = im.size
        f, e = os.path.splitext(target)

        if w>h:
           newwidth:int = round(w*thumbsize[0]/h)
           newheight:int = thumbsize[1]
           newsize:tuple = (newwidth,newheight)
           imresized = im.resize(newsize,Image.Resampling.LANCZOS)
           imresized.save(f+'Resized'+str(i)+'.jpg', "JPEG", quality=100)
           i += 1

        else:
            newwidth:int = thumbsize[0]
            newheight:int = round(h*thumbsize[0]/w)
            newsize:tuple = (newwidth,newheight)
            imresized = im.resize(newsize,Image.Resampling.LANCZOS)
            imresized.save(f+'Resized'+str(i)+'.jpg', "JPEG", quality=100)
            i += 1
        
            

def crop(source,target):
    
    files = os.listdir(source)

    i: int = 0
    for item in files:
        infile = os.path.join(source,item)      
        if os.path.isfile(infile):  #accept files and not folders, etc.
            im = Image.open(infile)
            w,h = im.size
            f, e = os.path.splitext(target)
            if w>h:
              offset:int = (w - thumbsize[0])/2
              imCrop = im.crop((offset, 0, thumbsize[0]+offset, thumbsize[1])) #corrected
              imCrop.save(f + 'Cropped'+str(i)+'.jpg', "JPEG", quality=100)
              i += 1
            elif h>w:
              offset:int = (h - thumbsize[1])/2
              imCrop = im.crop((0,offset, thumbsize[1], thumbsize[0]+offset)) #corrected
              imCrop.save(f + 'Cropped'+str(i)+'.jpg', "JPEG", quality=100)
              i += 1
            elif h==w:
              imCrop = im.crop((0, 0, thumbsize[0], thumbsize[1])) #corrected
              imCrop.save(f + 'Cropped'+str(i)+'.jpg', "JPEG", quality=100)
              i += 1

def tilesFormat(source,target):
   files = os.listdir(source)
   i:int = 0

   for item in files:
      f, e = os.path.splitext(target)
      infile = os.path.join(source,item)
      im = Image.open(infile).convert("L")
      brightness = ImageStat.Stat(im)
      im.save(f + "s" + str(i+1)+'.jpg', "JPEG", quality=100)
      i += 1

      sourceBrightness.append(("s" + str(i) + ".jpg",int(brightness.rms[0])))
   print("Average brightness for " + str(len(os.listdir(source))) + " source images: " + str(sourceBrightness))

   
def masterImgFormat(source,target):
      
      global rows
      global columns
      global collageWidth
      global collageHeight

      if len(os.listdir(source)) > 1:
         print("Master folder may contain only one image file, aborting")
      else:
         files = os.listdir(source)
         for item in files:
            infile = os.path.join(source,item)
            if os.path.isfile(infile):
               im = Image.open(infile).convert("L") #open image and convert to grayscale
               w,h = im.size
               f, e = os.path.splitext(target)
               collageWidth = round((w/thumbsize[0]))*thumbsize[0]
               collageHeight = round((h/thumbsize[1]))*thumbsize[1]
               newSize:tuple = (collageWidth,collageHeight)
               imResized = im.resize(newSize,Image.Resampling.LANCZOS) # resize to a multiple of thumbnail size
               print("Master image is "+ str(imResized.size[0])+ " pixel wide by " + str(imResized.size[1]) +" pixel high")

               columns= int(imResized.size[0]/thumbsize[0])
               rows= int(imResized.size[1]/thumbsize[1])

               print ("Final image will be made from "+ str(columns) + " columns and " + str(rows) + " rows")

               rowInc:int = 0
               i:int = 0
               while rowInc < rows:
                  rowOffset = rowInc * thumbsize[1]
                  columnInc:int = 0
                  while columnInc < columns:
                     columnOffset = columnInc * thumbsize[0]
                     imCrop = imResized.crop((columnOffset,rowOffset,columnOffset+thumbsize[0],rowOffset+thumbsize[1]))
                     imCrop.save(f + "c" + str(i+1) + ".jpg", "JPEG", quality=100)
                     i += 1
                     columnInc += 1
                     brightness = ImageStat.Stat(imCrop)
                     masterCropBrightness.append(("c" + str(i)+".jpg",int(brightness.rms[0])))

                  rowInc += 1

         print("Average brightness for " + str(len(os.listdir(target))) + " cropped images: " + str(masterCropBrightness))
                   
                  
def createMatch():

   global collageOrder

   i = 0
   sourceValues = [x[1] for x in sourceBrightness]
   sourceNames = [x[0] for x in sourceBrightness]
   croppedValues = [x[1] for x in masterCropBrightness]
   deltalist = []
   collageOrder = []

   for item in croppedValues:
     
      j = 0
      while j< len(sourceValues):
         delta = abs(croppedValues[i]-sourceValues[j])
         j += 1
         deltalist.append(delta)
      i += 1
      #print(deltalist)
      index_min = min(range(len(deltalist)), key=deltalist.__getitem__)
      #print(sourceNames[index_min])
      collageOrder.append(sourceNames[index_min])
      deltalist.clear()


def collate():
   collage = Image.new('L', (collageWidth,collageHeight))
   columnInc = 0
   rowInc = 0
   i = 0
   
   print(rows,columns)
   while rowInc < rows:
      while columnInc < columns:
         print()
         im = Image.open(os.path.join(greyedfolder,collageOrder[i]))
         collage.paste(im,(thumbsize[0]*columnInc,thumbsize[1]*rowInc))
         columnInc += 1
         i += 1
         print("columnSwitch")
         print(i)
      rowInc += 1
      columnInc = 0
      print("rowSwitch")
   collage.save(root+"collage.jpg", 'JPEG')
   collage.show
   print("all done!")
      
            


makeDir(resized_tiles_dir)
makeDir(cropped_resized_tiles_dir)
resize(tiles,resized_tiles)
crop(resized_tiles,cropped_resized_tiles)
makeDir(greyed_cropped_resized_tiles_dir)
tilesFormat(cropped_resized_tiles,greyed_cropped_resized_tiles)
makeDir(mastercropped)
masterImgFormat(master_image,master_image_cropped)
createMatch()
collate()
