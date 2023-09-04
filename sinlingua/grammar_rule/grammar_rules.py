from fuzzywuzzy import fuzz
from googletrans import Translator


class GrammarRules:
    @staticmethod
    # function for getting similarity score with similar word and actual word
    def find_similar_words(list_items, input_string):
        words = input_string.split()
        max_similarity = 0
        similar_word = None
        actual_word_of_string = None
        for line in list_items:
            line = line.strip()  # Remove leading/trailing whitespace
            for word in words:
                similarity_ratio = fuzz.ratio(word, line)
                if similarity_ratio >= 75 and similarity_ratio > max_similarity:
                    max_similarity = similarity_ratio
                    similar_word = line
                    actual_word_of_string = word  # Finally return similar word, similarity score and actual word
        return similar_word, actual_word_of_string, max_similarity

    def common_function(self, sentence):
        # Common implementation of the function
        pass

    @staticmethod
    # Check if returns output
    def output(output):
        if output != "Try Again..Incomplete sentence. No enough data to process":
            return output


def translate_sinhala_to_english(sentence):
    translator = Translator()
    translated = translator.translate(sentence, src='si', dest='en')
    return translated.text
