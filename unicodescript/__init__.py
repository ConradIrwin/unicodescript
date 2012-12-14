import os
import unicodedata
import bisect

scriptfile = os.path.dirname (os.path.abspath (__file__))+"/scripts.txt"

indexes = []
scripts = []
def script(char):
    """
        Gets the Unicode Script property of any character. Based on Scripts.txt from Unicode Consortium.
    """
    global scripts,indexes
    if not indexes:
        for line in open(scriptfile).readlines():
            indexes.append(int(line[:5],16))
            scripts.append(line[6:-1])
    try:
        key = ord(char)
    except:
        key = ord(unicodedata.normalize("NFC",char))

    return scripts[bisect.bisect_right(indexes, key)-1]


def inputloop():
    """
        Enter an interactive loop where the script of each character input (in utf-8) is printed.
    """
    while True:
        for char in raw_input().decode('utf-8'):
            print script(char)

if __name__ == "__main__":
    inputloop()
