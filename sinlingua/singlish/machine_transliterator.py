from sinlingua.singlish.rulebased_transliterator import RuleBasedTransliterator
from gensim.models import KeyedVectors


class MachineTransliterator(RuleBasedTransliterator):
    def __init__(self, model: str):
        """
        Initialize the MachineTransliterator.

        Parameters:
        -----------
        model: str
            Path to the FastText model file.

        Returns:
        --------
        None

        Example:
        --------
        >>> model_path = "../../resources/models/cc.si.300.vec"
        >>> transliterator = MachineTransliterator(model=model_path)
        """
        super().__init__()
        fasttext_path = model
        self.fasttext_model = KeyedVectors.load_word2vec_format(fasttext_path)

    def __get_best_suggestions(self, word: str) -> list:
        try:
            if word in self.fasttext_model:
                # Get most similar words from the FastText model
                most_similar_words = self.fasttext_model.most_similar(word)
                best_suggestions = [similar_word[0] for similar_word in most_similar_words]
                return best_suggestions
            else:
                return []
        except Exception as e:
            # Handle exceptions and return an empty list
            print(f"An error occurred while getting suggestions: {str(e)}")
            return []

    def transliterator(self, text: str) -> str:
        """
        Transliterate the input text using the rule-based approach and apply suggestions from the FastText model.

        This method takes Singlish text as input, transliterates it into the Sinhala script using the rule-based approach,
        and then applies word suggestions from the FastText model to enhance the transliteration quality.

        The method first uses the rule-based transliteration approach to convert Singlish text into Sinhala script.
        Then, for each word, it retrieves the best suggestions from the FastText model and replaces the original word
        with the top suggestion if available.

        Parameters:
        -----------
        text : str
            The Singlish text to be transliterated.

        Returns:
        --------
        str
            The transliterated text in the Sinhala script with FastText-based suggestions applied.

        Example:
        ---------
        >>> from sinlingua.singlish.rulebased_transliterator import RuleBasedTransliterator
        >>>
        >>> model_path = "../../resources/models/cc.si.300.vec"
        >>> transliterator = MachineTransliterator(model=model_path)
        >>> input_phrase = "oyaata kohomada"
        >>>
        >>> out = transliterator.transliterator(text=input_phrase)
        >>> print(out)
        ඔයාට කොහොමද

        Notes:
        ------
        - The method combines the rule-based and machine learning approaches for better transliteration results.
        - Make sure the FastText model has been initialized and loaded before calling this method.
        """
        try:
            # Call parent transliterator to get the initial output
            output = super().transliterator(text)

            # Process output word by word
            paragraphs = output.split('\n')
            similarity_paragraphs = []
            for paragraph in paragraphs:
                words = paragraph.split()
                similarity_words = []

                for word in words:
                    # Get the best suggestions for each word
                    best_suggestions = self.__get_best_suggestions(word)
                    if best_suggestions:
                        # Replace word with the best suggestion
                        suggested_word = best_suggestions[0]  # Assuming you only need the top suggestion
                        word = suggested_word
                    similarity_words.append(word)

                # Reconstruct the processed text
                processed_text = ' '.join(similarity_words)
                similarity_paragraphs.append(processed_text)

            output_text = '\n'.join(similarity_paragraphs)
            return output_text

        except Exception as e:
            # Handle exceptions and return the original input text
            print(f"An error occurred during transliteration: {str(e)}")
            return text