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
        self.consonants_without_a = data.get('consonants_without_a', {})
        self.special_consonants = data.get('special_consonants', {})
        self.dependent_vowels = data.get('dependent_vowels', {})
        self.dependent_vowels = data.get('dependent_vowels', {})

    def __split_into_logical_groups(self, word: str) -> str:
        try:
            logical_groups = []
            j = 0
            while j <= len(word):
                for length in range(4, 0, -1):
                    group = word[j: j + length]
                    if group in self.vowels:
                        logical_groups.append(self.vowels[group])
                        j += length
                        break
                    elif group in self.special_consonants:
                        logical_groups.append(self.special_consonants[group])
                        j += length
                        nested_group = word[j: j + 1].lower()
                        if nested_group == 'u':
                            logical_groups.append(self.dependent_vowels["Aa"])
                            j += 1
                            break
                        break
                    elif group in self.consonants:
                        logical_groups.append(self.consonants[group])
                        j += length
                        for nested_length in range(3, 0, -1):
                            nested_group = word[j: j + nested_length]
                            if nested_group in self.dependent_vowels:
                                logical_groups.append(self.dependent_vowels[nested_group])
                                j += nested_length
                                break
                        break
                    elif group in self.consonants_without_a:
                        logical_groups.append(self.consonants_without_a[group])
                        j += length
                        for nested_length in range(3, 0, -1):
                            nested_group = word[j: j + nested_length]
                            if nested_group in self.dependent_vowels:
                                logical_groups.append(self.dependent_vowels[nested_group])
                                j += nested_length
                                break
                        else:
                            logical_groups.append("්")
                        break
                    else:
                        if length != 1:
                            continue
                        else:
                            break
                else:
                    for length in range(4, 0, -1):
                        group = word[j: j + length]
                        group = group[0].lower() + group[1:]
                        if group in self.vowels:
                            logical_groups.append(self.vowels[group])
                            j += length
                            break
                        elif group in self.consonants:
                            logical_groups.append(self.consonants[group])
                            j += length
                            for nested_length in range(3, 0, -1):
                                nested_group = word[j: j + nested_length]
                                nested_group = nested_group[0].lower() + nested_group[1:]
                                if nested_group in self.dependent_vowels:
                                    logical_groups.append(self.dependent_vowels[nested_group])
                                    j += nested_length
                                    break
                            break
                        elif group in self.consonants_without_a:
                            logical_groups.append(self.consonants_without_a[group])
                            j += length
                            for nested_length in range(3, 0, -1):
                                nested_group = word[j: j + nested_length]
                                nested_group = nested_group[0].lower() + nested_group[1:]
                                if nested_group in self.dependent_vowels:
                                    logical_groups.append(self.dependent_vowels[nested_group])
                                    j += nested_length
                                    break
                            else:
                                logical_groups.append("්")
                            break
                        else:
                            if length != 1:
                                continue
                            else:
                                logical_groups.append(group)
                                j += 1
                                break
            return "".join(logical_groups)
        except Exception:
            return word

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
                sentences = paragraph.split(".")
                transliterated_sentences = []
                for sentence in sentences:
                    sentence = sentence.strip()
                    words = sentence.split()
                    transliterated_words = []
                    for word in words:
                        word = word.strip()
                        transliterated_words.append(self.__split_into_logical_groups(word))
                        print(transliterated_words)
                    transliterated_sentences.append(" ".join(transliterated_words))
                transliterated_paragraphs.append(". ".join(transliterated_sentences))
            transliterated_result = "\n".join(transliterated_paragraphs) + "."
            return transliterated_result

        except Exception as e:
            print(f"Error in transliterator method: {e}")
            return text
