# -*- coding: utf-8 -*-
from transformers import BertTokenizer, BertModel
import torch
from sinling import SinhalaTokenizer
from googletrans import Translator
import numpy as np
import string


punctuation = set(string.punctuation)
stopwords = ["සහ",
             "සමග",
             "සමඟ",
             "අහා",
             "ආහ්",
             "ආ",
             "ඕහෝ",
             "අනේ",
             "අඳෝ",
             "අපොයි",
             "අපෝ",
             "අයියෝ",
             "ආයි",
             "ඌයි",
             "චී",
             "චිහ්",
             "චික්",
             "හෝ‍",
             "දෝ",
             "දෝහෝ",
             "මෙන්",
             "සේ",
             "වැනි",
             "බඳු",
             "වන්",
             "අයුරු",
             "අයුරින්",
             "ලෙස",
             "වැඩි",
             "ශ්‍රී",
             "හා",
             "ය",
             "නිසා",
             "නිසාවෙන්",
             "බවට",
             "බව",
             "බවෙන්",
             "නම්",
             "වැඩි",
             "සිට",
             "දී",
             "මහා",
             "මහ",
             "පමණ",
             "පමණින්",
             "පමන",
             "වන",
             "විට",
             "විටින්",
             "මේ",
             "මෙලෙස",
             "මෙයින්",
             "ඇති",
             "ලෙස",
             "සිදු",
             "වශයෙන්",
             "යන",
             "සඳහා",
             "මගින්",
             "හෝ‍",
             "ඉතා",
             "ඒ",
             "එම",
             "ද",
             "අතර",
             "විසින්",
             "සමග",
             "පිළිබඳව",
             "පිළිබඳ",
             "තුළ",
             "බව",
             "වැනි",
             "මහ",
             "මෙම",
             "මෙහි",
             "මේ",
             "වෙත",
             "වෙතින්",
             "වෙතට",
             "වෙනුවෙන්",
             "වෙනුවට",
             "වෙන",
             "ගැන",
             "නෑ",
             "අනුව",
             "නව",
             "පිළිබඳ",
             "විශේෂ",
             "දැනට",
             "එහෙන්",
             "මෙහෙන්",
             "එහේ",
             "මෙහේ",
             "ම",
             "තවත්",
             "තව",
             "සහ",
             "දක්වා",
             "ට",
             "ගේ",
             "එ",
             "ක",
             "ක්",
             "බවත්",
             "බවද",
             "මත",
             "ඇතුලු",
             "ඇතුළු",
             "මෙසේ",
             "වඩා",
             "වඩාත්ම",
             "නිති",
             "නිතිත්",
             "නිතොර",
             "නිතර",
             "ඉක්බිති",
             "දැන්",
             "යලි",
             "පුන",
             "ඉතින්",
             "සිට",
             "සිටන්",
             "පටන්",
             "තෙක්",
             "දක්වා",
             "සා",
             "තාක්",
             "තුවක්",
             "පවා",
             "ද",
             "හෝ‍",
             "වත්",
             "විනා",
             "හැර",
             "මිස",
             "මුත්",
             "කිම",
             "කිම්",
             "ඇයි",
             "මන්ද",
             "හෙවත්",
             "නොහොත්",
             "පතා",
             "පාසා",
             "ගානෙ",
             "තව",
             "ඉතා",
             "බොහෝ",
             "වහා",
             "සෙද",
             "සැනින්",
             "හනික",
             "එම්බා",
             "එම්බල",
             "බොල",
             "නම්",
             "වනාහි",
             "කලී",
             "ඉඳුරා",
             "අන්න",
             "ඔන්න",
             "මෙන්න",
             "උදෙසා",
             "පිණිස",
             "සඳහා",
             "අරබයා",
             "නිසා",
             "එනිසා",
             "එබැවින්",
             "බැවින්",
             "හෙයින්",
             "සේක්",
             "සේක",
             "ගැන",
             "අනුව",
             "පරිදි",
             "විට",
             "තෙක්",
             "මෙතෙක්",
             "මේතාක්",
             "තුරු",
             "තුරා",
             "තුරාවට",
             "තුලින්",
             "නමුත්",
             "එනමුත්",
             "වස්",
             "මෙන්",
             "ලෙස",
             "පරිදි",
             "එහෙත්"]  # define the sinhala stop word list


class BertTextSummarizer:
    def __init__(self):
        self.tokenizer = SinhalaTokenizer()
        self.stopwords = stopwords
        self.punctuation = punctuation
        self.bert_tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
        self.bert_model = BertModel.from_pretrained('bert-base-multilingual-uncased')

    def __preprocess_sentences(self, text_corpus):
        try:
            sentences = self.tokenizer.split_sentences(text_corpus)
            sentences = [sent.strip() for sent in sentences]
            cleaned = [sent for sent in sentences if sent not in self.stopwords and sent not in self.punctuation]
            return cleaned, sentences
        except Exception as e:
            print(f"Error during preprocessing: {str(e)}")
            return [], []

    def __create_bert_embeddings(self, cleaned_sentences):
        sentence_embeddings = []
        for sent in cleaned_sentences:
            inputs = self.bert_tokenizer(sent, return_tensors="pt", max_length=512, truncation=True,
                                         padding='max_length')
            with torch.no_grad():
                output = self.bert_model(**inputs)
            sentence_embeddings.append(output.last_hidden_state.mean(dim=1).squeeze().numpy())

        if not sentence_embeddings:
            return np.array([]).reshape(0, self.bert_model.config.hidden_size)

        return np.array(sentence_embeddings)

    @staticmethod
    def __append_fullstop(text):
        if text and text[-1] not in punctuation:
            return text + '.'
        return text

    def __get_summary(self, top_n_sentences, sentences):
        try:
            sentence_organizer = {k: v for v, k in enumerate(sentences)}
            mapped_top_n_sentences = [(cleaned, sentence_organizer[cleaned]) for cleaned in top_n_sentences]
            mapped_top_n_sentences = sorted(mapped_top_n_sentences, key=lambda x: x[1])
            ordered_scored_sentences = [element[0] for element in mapped_top_n_sentences]
            summary = " ".join([self.__append_fullstop(sentence) for sentence in ordered_scored_sentences])
            return summary
        except Exception as e:
            print(f"Error during summary extraction: {str(e)}")
            return ""

    def summarize_by_percent(self, text_corpus, percent):
        """
        Summarize a given text based on a specified percentage.

        This method takes a text corpus and summarizes it by selecting the most important sentences based on the embeddings generated using BERT,
        until the desired percentage of the original text's length is reached.

        Parameters:
        -----------
        text_corpus : str
            The text to be summarized.
        percent : float
            The percentage of the most important sentences to be included in the summary. Values should be between 0 and 100.

        Returns:
        --------
        str
            The summarized text.

        Examples:
        ---------
        >>> from sinlingua.summarizer.bert import BertTextSummarizer
        >>> text_summarizer = BertTextSummarizer()
        >>> sample_text = "..."
        >>> summary = text_summarizer.summarize_by_percent(sample_text, percent=50)
        >>> print(summary)

        Notes:
        ------
        - Ensure that the text_corpus is preprocessed for best summarization results.
        - The returned summary will have sentences ordered as they appear in the original text.
        - Ensure the percentage value is between 0 and 100 for accurate results.
        """
        if not (0 <= percent <= 100):
            raise ValueError("Percent value should be between 0 and 100")
        cleaned_sentences, sentences = self.__preprocess_sentences(text_corpus)
        sentence_embeddings = self.__create_bert_embeddings(cleaned_sentences)

        if sentence_embeddings.size == 0:
            return ""

        sentence_scores = np.linalg.norm(sentence_embeddings, axis=1)
        N = int(len(cleaned_sentences) * percent / 100)
        top_n_sentences = [cleaned_sentences[ind] for ind in np.argsort(sentence_scores)[-N:]]
        return self.__get_summary(top_n_sentences, sentences)

    def summarize_by_word_count(self, text_corpus, word_count):
        """
        Summarize a given text  based on a specified word count limit.
        This method leverages the embeddings generated using BERT to rank the sentences in the text corpus by importance. It then selects the top-ranked sentences until the desired word count limit is reached.

        Parameters:
        -----------
        text_corpus : str
            The text to be summarized.
        word_count : int
            The maximum number of words desired in the summary. The method will select the most important sentences until this word limit is reached or exceeded.

        Returns:
        --------
        str
            The summarized text.

        Examples:
        ---------
        >>> from sinlingua.summarizer.bert import BertTextSummarizer
        >>> text_summarizer = BertTextSummarizer()
        >>> sample_text = "අද අප ඔබට කියන්නේ ටිකක් වෙනස් ආරක කතාවකි. මෙය සම්බන්ධ වන්නේ සෞඛ්‍ය ක්‍ෂේත්‍රයට ය. 2018 දෙසැම්බර් මාසයේදී චීනයේ වූහාන් නගරයේ වැසියන් අතර අමුතු ස්වසන රෝගයක් පැතිරෙමින් පවත්නා බව ලී වෙන්ලියෑං නමැති චීන වෛද්‍යවරයෙක් හෙළි කළේය. මේ රෝගය ඊට කලකට පෙර පැතිර ගිය සාර්ස් රෝගය හා සමාන බව එම දොස්තරගේ මතය විය. ඔහු ඒ ගැන සිය මිතුරන්ට දැන්වූ අතර ඒ පිළිබඳ ආරංචිය චීන බලධාරීන්ගේ කනට ගියේ ය. චීන ආණ්ඩුව ඔහු අත්අඩංගුවට ගත් අතර බොරු ආරංචි පතුරුවා චීනයේ කලබල ඇති කිරීමට තැත් කරන බව කියමින් හිර කූඩුවේද දැම්මේ ය. මෙයින් දින කීපයකට පසු කොවිඩ් 19 වැළඳී දොස්තර ලී මිය ගියේ ය. එබැවින් ඔහු බොරු කියා චීනය තුළ කැළඹීමක් ඇති කිරීමට තැත් නොකළ බව අලුතින්ම කීමට චීන ආණ්ඩුවට සිදුවිය."
        >>>
        >>> summary = text_summarizer.summarize_by_word_count(sample_text, word_count=30)
        >>> print(summary)

        Notes:
        ------
        - The method prioritizes retaining the semantic meaning of the original text. As a result, the returned summary might slightly exceed the specified word count limit.
        - Ensure that the text_corpus is preprocessed for optimal summarization results.
        - The returned summary will have sentences ordered as they appear in the original text.
        """

        cleaned_sentences, sentences = self.__preprocess_sentences(text_corpus)
        sentence_embeddings = self.__create_bert_embeddings(cleaned_sentences)

        if sentence_embeddings.size == 0:
            return ""

        sentence_scores = np.linalg.norm(sentence_embeddings, axis=1)
        sorted_sentences = [cleaned_sentences[ind] for ind in np.argsort(sentence_scores)[::-1]]

        N = 0
        total_words = 0
        for sent in sorted_sentences:
            total_words += len(sent.split())
            if total_words <= word_count:
                N += 1
            else:
                break
        top_n_sentences = sorted_sentences[:N]
        return self.__get_summary(top_n_sentences, sentences)

    @staticmethod
    def translate_to_english(text):
        """
        Translate a given Sinhala text (typically a summary) into English.

        This method uses the Google Translate API (through googletrans) to translate the given Sinhala text into English. It's typically used to translate the output of the `summarize_by_percent` or `summarize_by_word_count` methods.

        Parameters:
        -----------
        text : str
            The Sinhala text to be translated, often a summary produced by the other methods in this class.

        Returns:
        --------
        str
            The translated text in English.

        Examples:
        ---------
        >>> from sinlingua.summarizer.bert import BertTextSummarizer
        >>> text_summarizer = BertTextSummarizer()
        >>> sample_text = "අද අප ඔබට කියන්නේ ටිකක් වෙනස් ආරක කතාවකි. මෙය සම්බන්ධ වන්නේ සෞඛ්‍ය ක්‍ෂේත්‍රයට ය. 2018 දෙසැම්බර් මාසයේදී චීනයේ වූහාන් නගරයේ වැසියන් අතර අමුතු ස්වසන රෝගයක් පැතිරෙමින් පවත්නා බව ලී වෙන්ලියෑං නමැති චීන වෛද්‍යවරයෙක් හෙළි කළේය. මේ රෝගය ඊට කලකට පෙර පැතිර ගිය සාර්ස් රෝගය හා සමාන බව එම දොස්තරගේ මතය විය. ඔහු ඒ ගැන සිය මිතුරන්ට දැන්වූ අතර ඒ පිළිබඳ ආරංචිය චීන බලධාරීන්ගේ කනට ගියේ ය. චීන ආණ්ඩුව ඔහු අත්අඩංගුවට ගත් අතර බොරු ආරංචි පතුරුවා චීනයේ කලබල ඇති කිරීමට තැත් කරන බව කියමින් හිර කූඩුවේද දැම්මේ ය. මෙයින් දින කීපයකට පසු කොවිඩ් 19 වැළඳී දොස්තර ලී මිය ගියේ ය. එබැවින් ඔහු බොරු කියා චීනය තුළ කැළඹීමක් ඇති කිරීමට තැත් නොකළ බව අලුතින්ම කීමට චීන ආණ්ඩුවට සිදුවිය."
        >>>
        >>> summarized_text = text_summarizer.summarize_by_percent(sample_text, percent=20)
        >>> translated_text = text_summarizer.translate_to_english(summarized_text)
        >>> print(translated_text)

        Notes:
        ------
        - This method utilizes the unofficial Google Translate API (googletrans). Ensure you have a stable internet connection for best results.
        - For production-level applications, consider using the official Google Cloud Translation API.
        """
        try:
            translator = Translator()
            translation = translator.translate(text, src='si', dest='en')
            return translation.text
        except Exception as e:
            print(f"Error during translation: {str(e)}")
            return text


