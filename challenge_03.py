
"""
signed char from -128 to 127, and unsigned char from 0 to 255.
"""
import math
from PIL import Image, ImageFilter, ImageChops, ImageOps

if __name__ == "__main__":

    stuff = None

    with open(r'./hackfu2016/container/challenge 3/instructions.txt', 'rt') as handle:
        for index, line in enumerate(handle):
            if index == 4:
                # print(line)
                # ascii_ = line.encode('utf-8')
                # print(ascii_)
                # print(bytes.hex(ascii_))
                stuff = list()
                for item in line:
                    item = ord(item)
                    print(item)
                    if item > 127:
                        print(' ', 256-item)
                        stuff.append(256-item)
                    else:
                        stuff.append(item)

    # scale = 64
    # im = Image.new("L", (scale, scale))
    # im.putdata(stuff)
    # im.show()

    test = [chr(item) for item in stuff]
    print(''.join(test))
