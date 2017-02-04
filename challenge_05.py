"""
Challenge: Retrieve a phrase by assembling the string puzzle.
- feels like Hex?
- >> last digit is 0-f
- what do the first four letters represent?
- 25 dashes? Missing parts?
- are O = 0, I = 1? _ = ? (literally unknown -- maybe these make up the passkey? have to be guessed?)
-

"""
puzzle = ['OIOOb',
          '_IOI0',
          'OI_If',
          'IOOO6',
          '_OOO8',
          'I_II9',
          'II__3',
          '_IOO1',
          'O__I2',
          'OIOI9',
          'OOOOa',
          '_III8',
          'IOI_f',
          'OO_Of',
          'OIIIe',
          '_OIO0',
          'OOIOb',
          '_IO_1',
          '_IIO4',
          'IO_Oe',
          'OIO_d',
          '__IOc',
          'IIOIe',
          'O_OO4',
          'IIIId',
          'IOIO9',
          'IOOI8',
          'IO_Ic',
          'IO_I0',
          'IIIO8',
          'OO_I5',
          'OOII8']


def twist_into_byte(text):
    collector = []

    for item in text:

        if item == 'I':
            collector.append('1')
        elif item == 'O':
            collector.append('0')
        else:
            collector.append(item)

    return collector

print(len(puzzle))
for item in puzzle:
    _hex = int(item[-1], 16)
    _bin = bin(int(item[-1], 16))
    _byte = ''.join(twist_into_byte(item[:4]))

    try:
        print(item, _hex, ':\t', bin(int(_byte, 2)), _bin)
    except:
        pass

# manually lookinga the first line:
# 4bits, 4bits, hex, chr(hex), chr(4bits*4bits)
# produces 'K' maybe -- but this should be lower case, no spaces, no punctuation.
print(int('0b0100', 2), int('0b1011', 2), int('4b', 16), chr((int('4b', 16))), chr(4*11))

