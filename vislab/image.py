#import skimage
from skimage.io import imread

def get_image_for_filename(image_filename):
    if image_filename is not None:
        image = imread(image_filename)
        return image
    else:
        return None
