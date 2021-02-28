class Dictionary:

    def __init__(self):
        self.words = set()
        self.max_wordlen = 0

    def add_word(self, word):
        self.words.add(word.strip())

    def indexing(self):
        if len(self.words)>0:
            self.max_wordlen = max([len(word) for word in self.words])

    @classmethod
    def init_from_words(cls, words):
        d = cls()
        for w in words:
            d.add_word(w)
        d.indexing()
        return d

    @classmethod
    def init_from_runtime(cls):
        d = cls()

        try:
            n_words = int(input())
        except:
            n_words = 0

        while n_words > 0:
            d.add_word(input())
            n_words -= 1

        d.indexing()
        return d

    def parse_sentence_in_words(self, sentence):
        # todo: use word len as steps
        for i in range(min(len(sentence) + 1, self.max_wordlen + 1)):
            # print("in {}, check {}".format(sentence, sentence[:i]))
            if sentence[:i] in self.words and sentence[i:] in self.words:
                return [sentence[:i], sentence[i:]]
        return False

    def parse_sentence_in_words2(self, sentence):
        # todo: use word len as steps
        for i in range(min(len(sentence) + 1, self.max_wordlen + 1)):
            # print("in {}, check {}".format(sentence, sentence[:i]))
            if sentence[:i] in self.words:
                if len(sentence[i:]) == 0:
                    return [sentence[:i]]
                else:
                    words = self.parse_sentence_in_words2(sentence[i:])
                    if words:
                        words = [sentence[:i]] + words
                        return words
        return False

    def parse_sentence(self, sentence):
        # todo: directly produce words sen
        words = self.parse_sentence_in_words(sentence)
        return " ".join(words)


    def parse_from_runtime(self):
        try:
            n_sentences = int(input())
        except:
            n_sentences = 0

        res = []
        while n_sentences > 0:
            res.append(self.parse_sentence(input()))
            n_sentences -= 1
        return "\n".join(res) + "\n"


if __name__ == '__main__':
    # words = set(["hello", "world", "hell", "ow", "or"])
    # seq = "helloworld"

    # d = Dictionary.init_from_words(words)
    # print(d.parse_sentence(seq))

    d = Dictionary.init_from_runtime()
    print(d.parse_from_runtime())
