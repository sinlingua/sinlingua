# -*- coding: utf-8 -*-
import os
import functools
from typing import Union
import pygtrie as trie
from sinlingua.config import RESOURCE_PATH
from sinlingua.src.preprocessor_resources import suffix_list_dependent_vowels, suffixes_list, stem_dictionary

dependent_vowels = {
    "අ": "ා",
    "ආ": "ා",
    "ඇ": "ැ",
    "ඈ": "ෑ",
    "ඉ": 'ි',
    "ඊ": 'ී',
    "උ": 'ු',
    "ඌ": 'ූ',
    "එ": 'ෙ',
    "ඒ": 'ේ',
    "ඔ": 'ො',
    "ඕ": 'ෝ'
}


def _load_stem_dictionary():
    stem_list = []
    with open(os.path.join(RESOURCE_PATH, 'stem_dictionary.txt'), 'r', encoding='utf-8') as fp:
        for line in fp.read().split('\n'):
            try:
                base, suffix = line.strip().split('\t')
                stem_list.append([base, suffix])
            except ValueError as _:
                pass
    return stem_list


def _load_suffixes(file: str):
    suffixes = trie.Trie()
    with open(os.path.join(RESOURCE_PATH, file), 'r', encoding='utf-8') as fp:
        for suffix in fp.read().split('\n'):
            suffixes[suffix[::-1]] = suffix
    return suffixes


def _load_lists(file: str) -> list:
    with open(os.path.join(RESOURCE_PATH, file), 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Read all lines into a list
    lines = [line.strip() for line in lines]
    return lines


class SinhalaStemmer:
    def __init__(self):
        super().__init__()
        self.stem_list = stem_dictionary
        # self.suffixes = _load_suffixes(file='suffixes_list.txt')
        self.suffixes_normal = suffixes_list
        self.suffixes_dependent_vowels = suffix_list_dependent_vowels

    def step_one(self, text: str):
        for items in self.stem_list:
            if items[0] == text:
                return items[1]
            else:
                return text

    def step_two(self, text: str) -> str:
        for subtext in self.suffixes_normal:
            if text.endswith(subtext):
                last_index = text.rfind(subtext)
                modified_text = text[:last_index] + text[last_index + len(subtext):]
                return modified_text
        return text

    def step_three(self, text: str) -> str:
        for subtext in self.suffixes_normal:
            before_subtext = subtext[:1]
            subtext = subtext[1:]
            if text.endswith(subtext):
                last_index = text.rfind(subtext)
                modified_text = text[:last_index] + text[last_index + len(subtext):]
                if before_subtext in dependent_vowels:
                    modified_text = modified_text + dependent_vowels[before_subtext]
                    return modified_text
        return text

    def step_four(self, text: str) -> str:
        for subtext in self.suffixes_dependent_vowels:
            if text.endswith(subtext):
                last_index = text.rfind(subtext)
                modified_text = text[:last_index] + text[last_index + len(subtext):]
                return modified_text
        return text

    # def stem(self, word):
    #     if word in self.stem_dictionary:
    #         return self.stem_dictionary[word]
    #     else:
    #         suffix = self.suffixes.longest_prefix(word[::-1]).key
    #         if suffix is not None:
    #             return word[0:-len(suffix)], word[len(word) - len(suffix):]
    #         else:
    #             return word, ''

    @functools.singledispatchmethod
    def stemmer(self, x: Union[str, list]):
        raise NotImplementedError

    @stemmer.register(str)
    def _stemmer_(self, x: str):
        stemmed_list = []
        paragraphs = x.split("\n")
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            sentences = paragraph.split(".")
            for sentence in sentences:
                sentence = sentence.strip()
                words = sentence.split(" ")
                for word in words:
                    word = word.strip()
                    step1_out = self.step_one(text=word)
                    if step1_out == word:
                        step2_out = self.step_two(text=step1_out)
                        step3_out = self.step_three(text=step2_out)
                        step4_out = self.step_four(text=step3_out)
                        stemmed_list.append(step4_out)
                        continue
                    stemmed_list.append(step1_out)
        return stemmed_list

    @stemmer.register(list)
    def _stemmer_(self, x: list):
        stemmed_list = []
        for word in x:
            word = word.strip()
            step1_out = self.step_one(text=word)
            print(step1_out)
            if step1_out == word:
                step2_out = self.step_two(text=step1_out)
                step3_out = self.step_three(text=step2_out)
                stemmed_list.append(step3_out)
                continue
            stemmed_list.append(step1_out)
        return stemmed_list


if __name__ == "__main__":
    stemmer_obj = SinhalaStemmer()

    input = "විදුලි බිල හා ජල බිල තුන් හතර ගුණයකින් වැඩිවී, වැඩි කලක් යන්නට මත්තෙන් නැවත විදුලි අර්බුදයක හා ජල අර්බුදයක බර ජනතාවගේ හිස මත කඩා වැටී ඇත. විදුලිඅර්බුද මේ ඊයේ පෙරේදා දෙවනවරටත් ජල ගාස්තු සියයට 50 කට වැඩි ගණනකින් වැඩිකර ඇත. එසේම, නුදුරු අනාගතයේම විදුලි කප්පාදුවකට රජය අර අඳින බව පෙනෙන්නට තිබේ. අමාත්‍ය කංචන විජේසේකරගේ කතා බහෙන්ද ඒ බව ඉඟි කෙරේ. මීට හේතුව රටට බලපා ඇති දැඩි නියං තත්ත්වයයි. මේ නිසා ජල සහ විදුලි කප්පාදුවක් ළඟ ළඟම එන බව අප සියල්ලෝම තේරුම් ගත යුතුව"
    output = stemmer_obj.stemmer(input)
    print(output)
