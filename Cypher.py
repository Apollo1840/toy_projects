from collections import Counter


def get_input_sen():
    input_sen = ""

    try:
        n_lines = int(input())
    except:
        n_lines = 0

    while n_lines > 0:
        input_sen += input() + "\n"
        n_lines -= 1
    return input_sen


def cypher_book(input_sen):
    # char_book = [(char, freq) for char, freq in Counter(input_sen).items()]
    char_book = sorted(Counter(input_sen).items(), key=lambda x: x[0])
    char_book = sorted(char_book, key=lambda x: x[1])
    chars = [cf[0] for cf in char_book]
    cypher_book = dict([(char, code) for char, code in zip(chars, reversed(chars))])
    return cypher_book


if __name__ == "__main__":
    # input_sen = "Aliens are dumb¶"
    input_sen = get_input_sen()
    # input_sen = input_sen.replace("¶", "\n")
    cypher_book = cypher_book(input_sen)
    output_sen = "".join([cypher_book[c] for c in input_sen])
    # output_sen = output_sen.replace("\n", "¶")
    print(output_sen)
