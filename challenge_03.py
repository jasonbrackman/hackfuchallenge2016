
#
# - signed char from -128 to 127, and unsigned char from 0 to 255.
# - maybe we need to some frequency analysis? https://en.wikipedia.org/wiki/Frequency_analysis
#

import math
import binascii
import codecs
from PIL import Image, ImageFilter, ImageChops, ImageOps


def create_luminance_image_from_pixel_values(pixels, scale=(64, 64)):
    im = Image.new("L", scale)
    im.putdata(pixels)
    im.show()


def twos_complement(input_value, num_bits):
    '''Calculates a two's complement integer from the given input value's bits'''
    mask = 2**(num_bits - 1)
    return -(input_value & mask) + (input_value & ~mask)


def convert_to_signed(value):
    if value >= 128:
        return (255-value) * -1
    else:
        return 255 - value


def print_rotated_text(text):
    for index in range(150, 223):
        try:
            chars = [chr(twos_complement(item, 8) + index) for item in text]
            print(index, ': ', ''.join(chars), end='\n')

            # print(index, ': ', binascii.a2b_base64(''.join(chars)))

            # signed_chars = [chr(convert_to_signed(item) + index) for item in text]
            # print(index, ': ', ''.join(signed_chars), end='\n')

        except ValueError:
            pass

from collections import Counter


def letter_frequency(text='./hackfu2016/container/challenge 1/books/emma'):
    with open(text, 'rt') as handle:
        text = handle.read()
        count = Counter(text)

        totals = sum(count.values())

        frequency = {k: v/totals for k, v in count.items()}

        keys = reversed(sorted(frequency, key=lambda x: frequency[x] if frequency[x] is not None else 0))
        letter_frequency = {key: frequency[key] for key in keys}

        return letter_frequency


def align_frequency_of_text_to_english_distribution(text):
    letters = letter_frequency()
    encrypt = letter_frequency(r'./hackfu2016/container/challenge 3/instructions.txt')

    english = list(letters.keys())
    crypted = list(encrypt.keys())

    print(len(english))
    print(len(crypted))

    for x in range(1):
        result = list()
        for item in text:
            try:
                index = crypted.index(item) + x
                if index <= len(english):
                    result.append(english[index])
                else:
                    result.append("__")
            except:
                pass
        lines = ''.join(result).split("__")
        for line in lines:
            print(line)

if __name__ == "__main__":

    stuff = None
    with codecs.open(r'./hackfu2016/container/challenge 3/instructions.txt', 'rb') as handle:
        for index, line in enumerate(handle):
            if index == 4:
                print(line)
                print(line.decode())
                #align_frequency_of_text_to_english_distribution(line.decode())
                stuff = [item for index, item in enumerate(line) if not index % 2 == 0]
                import gzip
                from io import BytesIO
                buf = BytesIO(line)
                f = gzip.GzipFile(fileobj=buf).read()
                print(f)

    # is it a rotated cypher based on the signed/unsigned number?
    print_rotated_text(stuff)

    pixels = [convert_to_signed(item) for item in stuff]
    # create_luminance_image_from_pixel_values(pixels, scale=(128, 32))
    print(max(stuff))
    print(min(stuff))
    for index, item in enumerate(stuff):
        if max(stuff) == item:
            print(index, item)
    create_luminance_image_from_pixel_values(stuff, scale=(20, 210))


