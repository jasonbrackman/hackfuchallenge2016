import os

# There are 50 books
#
# could be:
# page, word  >> no way to know the page number
# lines down, characters in? >> not all texts satisfy the character depth
# character #, book # alphabetically? --> looked like gibberish
# liens down and the word? (arnold cypher?)
# words in, then another set of characters?
# Sort by Ebook # -- (characters in, ebook order?)


treasure = [(85, 8),
            (124, 11),
            (1984, 8),
            (3, 5),
            (901, 1),
            (3, 13),
            (8546, 12),
            (5, 2),
            (3, 4),
            (85, 10),
            (3437, 7)]

book_dir = './hackfu2016/container/challenge 1/books'

def get_words_01(path):
    letters = []
    with open(path, 'rt') as handle:
        lines = handle.readlines()
        for item in treasure:
            for index, line in enumerate(lines, 1):

                if index == item[0]:
                    # print(index, line)
                    try:
                        word = line.split()[item[1] + 1]
                        letters.append(word)
                    except:
                        letters.append('_')

    return ''.join(letters)


def get_letters_01(path):
    #print(path)
    letters = []
    with open(path, 'rt') as handle:
        lines = handle.readlines()
        for item in treasure:
            for index, line in enumerate(lines, 1):

                if index == item[0]:
                    #print(index, line)
                    try:
                        letters.append(line[item[1]+1])
                    except:
                        letters.append('_')

    return ''.join(letters)


def test_01():
    books = os.listdir(book_dir)
    for book in books:
        book_path = os.path.join(book_dir, book)
        print(get_letters_01(book_path))

#test_01()

def get_info():
    books = os.listdir(book_dir)
    for book in books:
        with open(os.path.join(book_dir, book), 'rt') as handle:

            lines = handle.readlines()
            # handle.seek(0)
            # words = handle.read().split()
            #
            # print('Line Length: ', len(lines))
            # paragraphs = [line for line in lines if len(line) < 3]
            # print('Para Length: ', len(paragraphs))
            # characters = [len(line) for line in lines]
            # print('Char Length: ', sum(characters))
            # print('Word Length: ', len(words))

            ebook = [line.split("#")[1].strip("['']\n") for line in lines if ' #' in line]
            ebook = [num.split(',] ')[0] for num in ebook]
            print('Book Number: ', sorted(ebook))


    letters = []
    for item in treasure:
        book = os.path.join(book_dir, books[item[1]-1])

        with open(book, 'rt') as handle:
            letter = handle.read()[item[0] -1]
            print(book, item[0]-1, letter)

            letters.append(letter)
    print('test02: ', ''.join(letters))

get_info()