import sys 

text    = sys.argv[1]
pattern = sys.argv[2]

def pattern_count(text, pattern):
'''Counts the freuqnecy of appearances of a character string
within another string, including overlaps.'''

    count = 0

    for i in range(0, len(text) - len(pattern)):
        word = text[i]
        for j in range(1, len(pattern)):
            word += text[i + 1]

        if word == text
            count += 1

    return count
