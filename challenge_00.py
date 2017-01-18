import binascii
from subprocess import Popen, PIPE

message = b"""U2FsdGVkX1/G1KRji4T1etFTkU0kA2DGNUoK3d/c+UeL1xOJhoa6WzA4NU78TwbF
/9Tofrgrk06+5D816A5EkRWGEPNfnu/kWpZPt4GgspQQ4qAsFu6IJ/Y3Bab+YARM
nzWKuSgOTJGUHhnmhHG4wk7yaBldp8fPHQ+MrBFAa3H3fpOOz6WxFVG1dGmJjoII
TVI94nX687oGVgktnRrVVCzILxPVISe9t4R/aiXAN2bku3+c63/InWMPR3j0181k
AabAszX8UWGGQS6QKnlE9VhMl9ZYJ3WdrfA/cVD9SYKoLEhsABNQpapR8eRcbkdV
2CKt9cMHIBFgMN4yXRAcyrjD0H3KuoP9Fbg0HMAcBDfBm/mtz9dX98GlLI4jy4sF
XZf7dwRKbqMXrlz8MwckuW45cxI6bsZdni62RJsbB0LaBzoBR/IjYT7YPkytxZbu
WBFJYI+oZOOojeWc1tSL3eSSMYTg/evoKaJB8j/HwD2xBw/+bTqAGPwaqfBALyo9
rD4LmpNjugiXWR2hfRj3m8ZrVkqGHCSc9t/RZWJTPdI6cxw7a46eLlJT0jjpCquD
ypflzJUzMzH0vl2LP1IY05FRdJ+ybYssiAB3rPc+o507Lh+VH07rTZOUzj0wDHxS
NQoO+jX3GiNBc+AfYYGhUbeuaKMENmVg5NH00PQm2YsX1pIbd9Wh/dBLeoA6fMcj
G+SlJzQdoLKfCAS8MkLny1D3Glg0xCF8RQqOWRtFPYhv65D/0O+Vr+WN89x4mdA2
3E1h3ywKgSD/WUlVzyjftfAxcNi5x1yvCaPgK9A+HYBi6TWpp5XvW/zdV4wlPHog
07Gz8eRfH0UZSD3SbA6ykWfVZ8xWM3NABZb1qiZJ+Zu8cUXPmI0gblM7SRZLwCrI
b9q8J2i01jlMvxZLS6Ua6wP560FqQxaTII6OE4KRoTbQ7k3+DDDFNW/qoAGzxK1c
DJKKzTcqVRD+vZWTbS6paytmAwl0ikViZfqVXgJZTUaB3J4jrddIFtQ2B+6hWvv2
SUOm1L6o1tkZ17iH105IXCe6BFNcTBe/i8rcSQkS7c2pZDY4AWmf32DaP7hhmg6z"""

message = binascii.a2b_base64(message)


def decrypt_openssl(infile=None, outfile=None, passphrase=None):

    cmd = f'openssl enc -d -base64 -aes-256-cbc -salt'.split()

    if infile:
        cmd += ['-in', infile]

    if outfile:
        cmd += ['-out', outfile]

    cmd += ['-k', passphrase]

    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()

    return out, err

if __name__ == "__main__":
    key = 'hackfuchallenge2016'
    filein = './hackfu2016/00.aes'
    print(decrypt_openssl(infile=filein, passphrase=key))

    #  This revealed the new key for the zip file -- already unlocked so the following is commented out
    #
    # key = "thedesolatewastelandawaitsyourarrival"
    # cmd = f'openssl enc -d -base64 -aes-256-cbc -salt -in ./hackfu2016/container.zip.aes -out ./hackfu2016/container.zip -k {key}'.split()
    # p = Popen(cmd, stdin=PIPE, stdout=PIPE)
    # out, err = p.communicate()
    # print(out)

