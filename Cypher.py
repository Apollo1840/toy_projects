# your code goes here
# your code goes here
from collections import Counter
import sys


def get_input_sen():
    sys.stdin.readline()
    input_sen = ""
    input_sen += sys.stdin.read()
    return input_sen


def cypher_book(input_sen):
    char_book = [(char, freq) for char, freq in Counter(input_sen).items()]
    # char_book = sorted(Counter(input_sen).items(), key=lambda x: x[0])
    # char_book = sorted(char_book, key=lambda x: x[1])
    char_book = sorted(char_book, key=lambda x: ord(x[0]) + 256 * x[1])
    chars = [cf[0] for cf in char_book]
    cypher_book = dict([(char, code) for char, code in zip(chars, reversed(chars))])
    return cypher_book


if __name__ == "__main__":
    # input_sen = "Aliens are dumb¶"
    input_sen = get_input_sen()
    cypher_book = cypher_book(input_sen)
    output_sen = "".join([cypher_book[c] for c in input_sen])
    print(output_sen, end='')