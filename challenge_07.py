# opened the doc file in textedit -- there was some english text

import challenge_00
passphrase = r'youcannotspellscorchedearthwithoutdeath'
#passphrase = r'youcannotspellscorchedearthwithoutth'
print(challenge_00.decrypt_openssl('./hackfu2016/container/challenge 7/solution.txt.enc',
                                   './hackfu2016/container/challenge 7/solution.txt',
                                   passphrase=passphrase))
