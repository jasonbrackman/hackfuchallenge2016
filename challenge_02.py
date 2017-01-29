# feels like a stenography challenge
# Its an L Mode image - (8-bit pixels, black and white)
# The text in the image (without doing anything appears to say 'lo filter sim' or 'co filter sim')
# --> note that it might actually be 'lo filter s1m': s1m is something i've seen mentioned alongside RSA
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

from PIL import Image, ImageChops
import challenge_00


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


def combine_images_for_every_second_value():
    im = Image.open('./hackfu2016/container/challenge 2/image')

    even_image = None

    for index in range(255):
        if index % 2 == 0:
            new_data = get_new_data(im, index)
            temp_im = Image.new(im.mode, im.size)
            temp_im.putdata(new_data)

            if even_image is None:
                even_image = temp_im
            else:
                even_image = ImageChops.add_modulo(even_image, temp_im)

    return even_image


if __name__ == "__main__":
    image = combine_images_for_every_second_value()
    image.save('./challenge_02_output/even.bmp')

    # used an online service to read the QR code
    passphrase = 'theleastsignificantisthemostsignificant'

    print(challenge_00.decrypt_openssl('./hackfu2016/container/challenge 2/solution.txt.enc',
                                       './challenge_02_output/solution.txt',
                                       passphrase=passphrase))
