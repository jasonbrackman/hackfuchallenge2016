
"""
signed char from -128 to 127, and unsigned char from 0 to 255.
"""
import math
import binascii
import codecs
from PIL import Image, ImageFilter, ImageChops, ImageOps


def create_luminance_image_from_pixel_values(pixels, scale=64):
    im = Image.new("L", (scale, scale))
    im.putdata(pixels)
    im.show()


def convert_to_signed(value):
    if value >= 128:
        return (255-value) * -1
    else:
        return 255 - value


def print_rotated_text(text):
    for index in range(-100, 200):
        try:
            chars = [chr(item + index) for item in text]
            print(index, ': ', ''.join(chars), end='\n')
            # print(index, ': ', binascii.a2b_base64(''.join(chars)))

            # signed_chars = [chr(convert_to_signed(item) + index) for item in text]
            # print(index, ': ', ''.join(signed_chars), end='\n')

        except ValueError:
            pass


if __name__ == "__main__":

    stuff = None

    with codecs.open(r'./hackfu2016/container/challenge 3/instructions.txt', 'rb') as handle:
        for index, line in enumerate(handle):
            if index == 4:
                print(line)
                stuff = [item for index, item in enumerate(line) if not index % 2 == 0]

    # is it a rotated cypher based on the signed/unsigned number?
    print_rotated_text(stuff)

    # pixels = [convert_to_signed(item) for item in stuff]
    # create_luminance_image_from_pixel_values(pixels)
    # create_luminance_image_from_pixel_values(stuff)

