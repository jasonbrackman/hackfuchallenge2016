# feels like a stenography challenge
# Its an L Mode image - (8-bit pixels, black and white)
# The text in the image (without doing anything appears to say 'lo filter sim' or 'co filter sim')
# there is also a #2 on the top of the forehead of the mask/filter
# --> maybe I need to do a filter on the image?
# --> low pass filter is a blurring operation.
# """ Although the LSB embedding methods hide data in such a way that the humans do not
#   perceive it such schemes can be easily destroyed by an opponent, using for example lossy
#   compression algorithms or a filtering process. Any process that performs, directly or indirectly,
#   a low pass filtering can easily eliminate the data placed on the high frequency spectrum. One
#   possible countermeasure is to use error correction codes or to hide data in more than one
#   location. """
#
import os
from collections import Counter
from PIL import Image, ImageFilter, ImageChops, ImageOps
import challenge_00


def get_image_info(im):
    print(im.histogram())
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


def get_new_data(im, value):
    width, height = im.size

    new_data = []
    for w in range(width):
        for h in range(height):

            pixel = im.getpixel((h, w))
            if value == pixel:
                pixel = 255
            else:
                pixel = 0
            new_data.append(pixel)

    return new_data


def create_image(new_data, mode, size, index):
    im = Image.new(mode, size)
    im.putdata(new_data)
    im.save('img_{0:03d}.bmp'.format(index))


def gaussian_filter(im, ammount):

    #im2 = im.filter(ImageFilter.GaussianBlur(radius=ammount))
    im2 = ImageOps.unsharp_mask(im, ammount)
    im3 = ImageOps.box_blur(im, ammount)
    #im4 = ImageChops.add(im3, im2)

    # im2 = ImageOps.invert(im2)
    im3.show()

    # for index in range(0, 1000, 1000):
    #     #im2 = im.filter(ImageFilter.UnsharpMask(radius=2, percent=index, threshold=6))
    #     im2 = im.filter(ImageFilter.FIND_EDGES)
    #     im2.show()

    # im3 = ImageChops.add(, guassian)


    #im1 = im.filter(ImageFilter.BLUR)
    #im2 = im.filter(ImageFilter.MinFilter(3))
    #im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
    #im3.show()


def generate_images_for_each_value():
    im = Image.open('./hackfu2016/container/challenge 2/image')
    get_image_info(im)

    for index in range(255):
        new_data = get_new_data(im, index)
        create_image(new_data, im.mode, (840, 840), index)


def combine_images(path):
    even = None
    # odd = None
    files = os.listdir(path)
    for file in files:
        file, ext = os.path.splitext(file)
        value = int(file.split('_')[1])

        new_image = Image.open(os.path.join(path, file + '.bmp'))

        if value % 2 == 0:
            if even is None:
                even = new_image
            else:
                even = ImageChops.add_modulo(even, new_image)
        # else:
        #     if odd is None:
        #         odd = new_image
        #     else:
        #         odd = ImageChops.add_modulo(odd, new_image)

    even.save('even.bmp')
    # odd.save('odd.bmp')


if __name__ == "__main__":
    passphrase = 'theleastsignificantisthemostsignificant'
    print(challenge_00.decrypt_openssl('./hackfu2016/container/challenge 2/solution.txt.enc',
                                       './challenge_02_output/solution.txt',
                                       passphrase=passphrase))
    pass
    # generate_images_for_each_value()
    # combine_images('./images_per_pixel_value')
