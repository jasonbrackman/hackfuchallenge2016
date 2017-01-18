# feels like a stenography challenge
# Its an L Mode image - (8-bit pixels, black and white)
# The text in the image (without doing anything appears to say 'lo filter sim' or 'co filter sim'
# --> maybe I need to do a filter on the image?
# --> low pass filter is a blurring operation.
# """ Although the LSB embedding methods hide data in such a way that the humans do not
#   perceive it such schemes can be easily destroyed by an opponent, using for example lossy
#   compression algorithms or a filtering process. Any process that performs, directly or indirectly,
#   a low pass filtering can easily eliminate the data placed on the high frequency spectrum. One
#   possible countermeasure is to use error correction codes or to hide data in more than one
#   location. """
#

from collections import Counter
from PIL import Image, ImageFilter


def get_image_info(im):
    print('bands: ', im.getbands())
    for item in im.__dict__:
        print(item, getattr(im, item))
    width, height = im.size
    pixel_values = list(im.getdata())
    count = Counter(pixel_values)
    print(count.most_common(5))
    for y in range(0, height):  # each pixel has coordinates
        row = ""
        for x in range(0, width):
            RGB = im.getpixel((x, y))
            # print(RGB)
            # R, G, B = RGB  # now you can use the RGB value
            # print(R)

def get_pixle_data_divisible_by(im, number):
    width, height = im.size

    new_data = []
    for w in range(width):
        for h in range(height):

            pixel = im.getpixel((h, w))
            if 66 < pixel < 105:
                pixel = 0
            else:
                pixel = 255
            new_data.append(pixel)

    return new_data


def create_image(new_data, mode, size):
    im = Image.new(mode, size)
    im.putdata(new_data)
    im.show()

def gaussian_filter(im, ammount):


    #im1 = im.filter(ImageFilter.BLUR)
    #im2 = im.filter(ImageFilter.MinFilter(ammount))
    #im3 = im2.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
    #im2 = im.filter(ImageFilter.GaussianBlur(radius=ammount))
    #im2 = im.filter(ImageFilter.UnsharpMask())
    im2 = im.filter(ImageFilter.MinFilter(size=ammount))
    #im1.show()
    im2.show()
    #im3.show()

if __name__ == "__main__":
    im = Image.open('./hackfu2016/container/challenge 2/image')
    get_image_info(im)
    data = im.getdata()
    number = 3
    new_data = get_pixle_data_divisible_by(im, number)

    #create_image(new_data, im.mode, (840, 840))
    gaussian_filter(im, number)
    if len(data)/2 == len(new_data):
        print(True)
    else:
        print(len(data), len(new_data))
