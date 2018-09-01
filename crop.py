
import os
from PIL import Image


SOURCE_DIR = "/" + str( input("Enter image set source : ")) + "/"
DEST_DIR = SOURCE_DIR + "crops/"

CROP_AREA = (66, 124, 1904, 1026)

#list of image filenames
for file_name in [ f for f in os.listdir(SOURCE_DIR) if os.path.isfile(SOURCE_DIR + f) ]:

    #open images
    try:
        img = Image.open( SOURCE_DIR + file_name)
    except OSError:
        continue

    assert ( img.size[0] >= CROP_AREA[2] and img.size[1] >= CROP_AREA[3]) , "Image is too small for defined crop area"

    #crop
    crop_img = img.crop(CROP_AREA)

    if not os.path.exists( DEST_DIR ):
        os.makedirs( DEST_DIR )

    if not os.path.isfile( DEST_DIR + file_name ):
        crop_img.save( DEST_DIR + file_name )



