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


def arnold_cypher(books, treasure):
    keys = list()
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

            keys.append(''.join(results))

        except Exception as e:
            pass

    return keys

if __name__ == "__main__":
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

    keys = arnold_cypher(books, treasure)
    for key in keys:
        out, err = challenge_00.decrypt_openssl(infile='./hackfu2016/container/challenge 1/solution.txt.enc',
                                                outfile='./hackfu2016/container/challenge 1/solution.txt',
                                                passphrase=key)

        if b"bad decrypt" not in err:
            print('Solution:', key)  # 'wemustembracethepainandburnitforourjourney'
            break