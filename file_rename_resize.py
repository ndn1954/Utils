from PIL import Image
import os, sys

def resizeImage(infile, output_dir="", size=(300,300)):
     outfile = os.path.splitext(infile)[0]
     extension = os.path.splitext(infile)[1]
     infile = os.path.join('<<folderpath>>',infile)

     if infile != outfile:
        try :
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save('<<folderpath>>'+outfile+extension,"JPEG")
        except IOError as ex:
            print ("cannot reduce for", infile)
            print (ex)


if __name__=="__main__":
    dir = "<<folderpath>>"

    for file in os.listdir(dir):
        resizeImage(file,output_dir)
