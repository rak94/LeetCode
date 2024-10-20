import re
from typing import List

class MostCommonWords:
    def most_common_words(self, paragraph = str, banned = List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())

        words = paragraph.split()

        banned_words = set(banned)

        word_dict = {}

        for word in words:
            if word not in banned_words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict = 1

        max_word = None
        max_count = 0

        for word, count in word_dict.items():
            if count > max_count:
                max_word = word
                max_count = count

        return max_word