import challenge_00
import os

# There are 50 books
#
# could be:
# page, word  >> no way to know the page number
# lines down, characters in? >> not all texts satisfy the character depth
# character #, book # alphabetically? --> looked like gibberish

# liens down and the word? (arnold cypher?) <-- this one isn't gibberish....

# words in, then another set of characters?
# Sort by Ebook # -- (characters in, ebook order?) - didn't work looks like gibberish


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
books = [os.path.join(book_dir, book) for book in os.listdir(book_dir)]


def arnold_cypher():
    for book in books:
        try:
            results = list()
            with open(book, 'rt') as handle:
                lines = handle.readlines()
                for item in treasure:
                    line_count, word_count = item
                    current_line = lines[line_count-1]
                    current_word = current_line.split(' ')[word_count-1]
                    results.append(current_word)

            key = ''.join(results)
            out, err = challenge_00.decrypt_openssl(infile='./hackfu2016/container/challenge 1/solution.txt.enc',
                                                    outfile='./hackfu2016/container/challenge 1/solution.txt',
                                                    passphrase=key)

            if b"bad decrypt" not in err:
                print('Solution:', key)
                break

        except Exception as e:
            pass


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
    matches = {}
    for book in books:
        with open(os.path.join(book_dir, book), 'rt') as handle:
            lines = handle.readlines()
            handle.seek(0)
            words = handle.read().split()

            print('Line Length: ', len(lines))
            paragraphs = [line for line in lines if len(line) < 3]
            print('Para Length: ', len(paragraphs))
            characters = [len(line) for line in lines]
            print('Char Length: ', sum(characters))
            print('Word Length: ', len(words))

            # ebook = [line.split("#")[1].strip("['']\n") for line in lines if ' #' in line]
            import re

            for line in lines:

                if 'ebook #' in line.lower() or 'etext #' in line.lower():
                    if book not in matches:
                        result= int(re.search(r'#\d+', line, re.I).group().strip('#'))
                        matches[book] = result

    books = sorted(matches.items(), key=lambda x: x[1])

    letters = []
    for index in treasure:
        character = index[0]-1
        book, _ = books[index[1]-1]
        # print(book, character)

        with open(os.path.join(book_dir, book), 'rt') as handle:
            letter = handle.read()[character]
            letters.append(letter)
    print('Reordered: ', ''.join(letters))

    books = os.listdir(book_dir)
    letters = []
    for item in treasure:
        book = os.path.join(book_dir, books[item[1]-1])

        with open(book, 'rt') as handle:
            letter = handle.read()[item[0] -1]
            #print(book, item[0]-1, letter)

            letters.append(letter)
    print('  ordered: ', ''.join(letters))

if __name__ == "__main__":
    arnold_cypher()