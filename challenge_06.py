# coding=utf-8
# - compressed so unlike #2 pixel accuracy is not likely :)
# -
# - Looks like a puzzle that needs to be rotated?
# Creation Date: 1/28/2017
#
# --------------------------------------------------------------------------------------

from PIL import Image, ImageOps
import challenge_00


def step_rotate_inner_dimensions(image, border):

    for index in range(image.size[0]):
        value = border*index
        if value < image.size[0]:
            region = ImageOps.crop(image, border=value)
            region = region.transpose(Image.ROTATE_90)
            image.paste(region, (value, value))

    return image

if __name__ == "__main__":

    image = Image.open('./hackfu2016/container/challenge 6/image.jpg')
    image = step_rotate_inner_dimensions(image, 10)
    # image.save('./hackfu2016/container/challenge 6/image_solution.jpg')
    image.show()
    passphrase = r'thefirststageofourrenewalisdestruction'
    print(challenge_00.decrypt_openssl('./hackfu2016/container/Challenge 6/solution.txt.enc',
                                       './hackfu2016/container/Challenge 6/solution.txt',
                                       passphrase=passphrase))




