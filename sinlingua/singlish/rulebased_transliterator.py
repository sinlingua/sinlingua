import json
import os
import pkg_resources
from sinlingua.src.singlish_resources import alphabet


class RuleBasedTransliterator:
    def __init__(self):
        """
        Initialize the RuleBasedTransliterator object.

        This constructor initializes the RuleBasedTransliterator object with the configuration data
        for vowels, consonants, and dependent vowels. It sets up the dictionaries needed for the
        transliteration process.

        Examples:
        ---------
        >>> from sinlingua.singlish.rulebased_transliterator import RuleBasedTransliterator
        >>>
        >>> transliterator = RuleBasedTransliterator()
        >>>
        >>> # The object is now initialized and ready to perform transliteration.
        """
        self.vowels = {}
        self.consonants = {}
        self.dependent_vowels = {}

        # alphabet = "singlish-alphabet.json"
        # data = self.__read_json_config(file_path=alphabet)
        data = alphabet
        self.vowels = data.get('vowels', {})
        self.consonants = data.get('consonants', {})
        self.dependent_vowels = data.get('dependent_vowels', {})

    def __split_into_logical_groups(self, word: str) -> list:
        logical_groups = []
        current_group = ''
        i = 0
        while i < len(word):
            try:
                for length in range(3, 0, -1):
                    if i + length <= len(word):
                        group = word[i:i + length]
                        if group in self.vowels:
                            logical_groups.append(self.vowels[group])
                            i += length

                for length in range(4, 0, -1):
                    if i + length <= len(word):
                        group = word[i:i + length]
                        if group in self.consonants:
                            logical_groups.append(current_group)
                            current_group = self.consonants[group]
                            i += length

                            if i >= len(word):
                                current_group = current_group + "්"
                                break
                            else:
                                for next_length in range(3, 0, -1):
                                    if i + next_length <= len(word):
                                        group = word[i:i + next_length]
                                        if group in self.dependent_vowels:
                                            logical_groups.append(current_group)
                                            current_group = self.dependent_vowels[group]
                                            i += next_length
                                            break
                                else:
                                    if i < len(word) and word[i] == "a":
                                        i += 1
                                    elif (word[i:i + 1] or word[i:i + 2] or word[i:i + 3] or word[i:i + 4]) in (self.consonants or self.vowels):
                                        current_group = current_group + "්"
                                        break
                                    else:
                                        # Handle unknown characters
                                        current_group += word[i]
                                        i += 1
                            break
                else:
                    # Handle unknown characters
                    current_group += word[i]
                    i += 1

                # Check for vowels
                for length in range(3, 0, -1):
                    if i + length < len(word):
                        group = word[i:i + length]
                        if group in self.vowels:
                            logical_groups.append(current_group)
                            current_group = self.vowels[word[i:i + 3]]
                            i += 3
                            break

                # # Check for dependent vowel signs
                # for length in range(3, 0, -1):
                #     print("Dependent Vowels")
                #     if i + length < len(word):
                #         group = word[i:i + length]
                #         if group in self.dependent_vowels:
                #             logical_groups.append(current_group)
                #             current_group = self.dependent_vowels[word[i:i + 3]]
                #             i += 3
                #             break

            except Exception as e:
                # Handle exceptions
                print(f"An error occurred: {str(e)}")
                return []

        if current_group:
            logical_groups.append(current_group)

        return logical_groups

    # @staticmethod
    # def __read_json_config(file_path: str) -> dict:
    #     try:
    #         json_file_path = pkg_resources.resource_filename('sinlingua', os.path.join('resources', file_path))
    #         # Read JSON configuration file and return the data as dictionary
    #         with open(os.path.join(json_file_path, file_path), 'r', encoding='utf-8') as json_file:
    #             json_data_c = json.load(json_file)
    #         return json_data_c
    #     except Exception as e:
    #         # Handle exceptions while reading JSON configuration
    #         print(f"Error while reading JSON configuration file '{file_path}': {str(e)}")
    #         return {}

    def transliterator(self, text: str) -> str:
        """
        Transliterate English text into the Sinhala script.

        This method takes English text as input and transliterates it into the Sinhala script.
        It separates the text into paragraphs and words, and transliterates each word individually.
        The transliterated text maintains the original paragraph structure.

        Parameters:
        -----------
        text : str
            The English text to be transliterated.

        Returns:
        --------
        str
            The transliterated text in the Sinhala script.

        Examples:
        ---------
        >>> from sinlingua.singlish.rulebased_transliterator import RuleBasedTransliterator
        >>>
        >>> transliterator = RuleBasedTransliterator()
        >>> input_phrase = "oyaata kohomadha"
        >>>
        >>> out = transliterator.transliterator(text=input_phrase)
        >>> print(out)
        ඔයාට කොහොමද

        Notes:
        ------
        - The method relies on the 'vowels', 'consonants', and 'dependent_vowels' dictionaries
          to perform the transliteration. Make sure these dictionaries are defined correctly
          in the configuration file before calling this method.
        - The method uses the 'split_into_logical_groups' helper function to split each word
          into logical groups based on the rules of Sinhala transliteration.
        """

        try:
            paragraphs = text.split('\n')
            transliterated_paragraphs = []

            for paragraph in paragraphs:
                words = paragraph.split()
                transliterated_words = []

                for word in words:
                    logical_groups = self.__split_into_logical_groups(word)

                    output = ''
                    for group in logical_groups:
                        if group in self.vowels:
                            output += self.vowels[group]
                        elif group in self.dependent_vowels:
                            output += self.dependent_vowels[group]
                        else:
                            output += group

                    transliterated_word = output
                    transliterated_words.append(transliterated_word)

                transliterated_paragraph = ' '.join(transliterated_words)
                transliterated_paragraphs.append(transliterated_paragraph)

            output_text = '\n'.join(transliterated_paragraphs)
            return output_text

        except Exception as e:
            print(f"Error in transliterator method: {e}")
            return text