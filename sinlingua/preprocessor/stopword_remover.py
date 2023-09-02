from sinlingua.src.preprocessor_resources import stop_words
import os


class StopWordRemover:
    def __init__(self):
        self.stop_words = stop_words

    def remove_stop_words(self, text):
        words = text.split()
        remaining_words = [word for word in words if word not in self.stop_words]
        remaining_text = ' '.join(remaining_words)
        return remaining_text



