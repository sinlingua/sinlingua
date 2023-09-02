# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
from sinling import SinhalaTokenizer
from googletrans import Translator
import numpy as np
import string


punctuation = set(string.punctuation)
stopwords = [
    "සහ",
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


class TFIDFTextSummarizer:
    def __init__(self):
        self.tokenizer = SinhalaTokenizer()
        self.stopwords = stopwords
        self.punctuation = punctuation

    def __preprocess_sentences(self, text):  # stopwords & punctuation handling
        try:
            sentences = self.tokenizer.split_sentences(text)
            sentences = [sent.strip() for sent in sentences]
            cleaned = [sent for sent in sentences if sent not in self.stopwords and sent not in self.punctuation]
            return cleaned, sentences
        except Exception as e:
            print(f"Error during preprocessing: {str(e)}")
            return [], []

    @staticmethod
    def __create_tfidf_model(cleaned_sentences):  # sentences vectorized by the tfidf method
        try:
            tf_idf_vectorizer = TfidfVectorizer(
                min_df=2, max_features=None, strip_accents='unicode', analyzer='word',
                token_pattern=r'\w{1,}', ngram_range=(1, 3), use_idf=1, smooth_idf=1, sublinear_tf=1,
            )
            tf_idf_vectorizer.fit(cleaned_sentences)
            sentence_vectors = tf_idf_vectorizer.transform(cleaned_sentences)
            return tf_idf_vectorizer, sentence_vectors
        except Exception as e:
            print(f"Error during TF-IDF model creation: {str(e)}")
            return None, []

    @staticmethod
    def __append_fullstop(text):   # Add fullstop for end of each sentences
        if text and text[-1] not in punctuation:
            return text + '.'
        return text

    def __get_summary(self, top_n_sentences, sentences):  # ordering sentences & make the summary
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

    def summarize_by_percent(self, text, percent):
        """
        Summarize a given text corpus based on a specified percentage.

        This method takes a text corpus and summarizes it by selecting the most important sentences until the desired percentage is reached.

        Parameters:
        -----------
        text_corpus : str
            The text to be summarized.
        percent : float
            The percentage of the original text to be retained in the summary.

        Returns:
        --------
        str
            The summarized text.

        Examples:
        ---------
        >>> from sinlingua.summarizer.tf_idf import TFIDFTextSummarizer
        >>> text_summarizer = TFIDFTextSummarizer()
        >>> sample_text = "පාර්ලිමේන්තුවේ කාර්ය මණ්ඩලයේ සිටින ඇතැම් කාන්තාවන් එම කාර්ය මණ්ඩලයේම සිටින පිරිමින් අතින් අපහරණයට ලක්වූ බව අප පසුගිය දිනයේ කියෙව්වෙමු. මේ පිළිබඳ පරීක්‍ෂා කිරීම සඳහා දැනටමත් සාමාජිකයන් තුන්දෙනකුගෙන් සමන්විත කමිටුවක් පත්කොට තිබේ. සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. මෙය ඉතා භයානක තත්ත්වයකි. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය. හඳුනාගත් වහාම ඔවුන්ගේ වැඩ තහනම් කළ යුතුය. කථානායකතුමා මේ කාර්යය සම්බන්ධයෙන් දැඩිව සිටින බව අපට විශ්වාසය. පාර්ලිමේන්තු මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි මෙය රට කරවන ප්‍රමුඛ ආයතනය වූ පාර්ලිමේන්තුවට එල්ල කරන ලද මඩ පහරකි. මේ පිළිබඳ තනිව නැගී සිට හඬ නැගීම ගැන රෝහිණී කවිරත්නට ස්තුතිවන්ත වෙමු. මේ අතර පසුගිය දිනවල පාර්ලිමේන්තුවේ මන්ත්‍රීවරියන්ට වාචිකව කරන ලද ලිංගික අඩන්තේට්ටම ගැනද දැනගන්නට ලැබිණ. යුද බිමේ තිබෙන ස්ත්‍රී අපහරණය නමැති නීච ආයුධය පාර්ලිමේන්තුව තුළට ගෙන ඒමට ඉඩදිය යුතු නැත."
        >>>
        >>> summary = text_summarizer.summarize_by_percent(sample_text, percent=20)
        >>> print(summary)
        සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය.

        Notes:
        ------
        - Ensure that the text_corpus is preprocessed for best summarization results.
        - The returned summary will have sentences ordered as they appear in the original text.
        """
        cleaned_sentences, sentences = self.__preprocess_sentences(text)
        _, sentence_vectors = self.__create_tfidf_model(cleaned_sentences)
        sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
        N = int(len(cleaned_sentences) * percent / 100)
        top_n_sentences = [cleaned_sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
        return self.__get_summary(top_n_sentences, sentences)

    def summarize_by_word_count(self, text, word_count):
        """
            Summarize a given text corpus based on a specified word count.

            This method takes a text corpus and summarizes it by selecting the most important sentences until the desired word count is reached.

            Parameters:
            -----------
            text_corpus : str
                The text to be summarized.
            word_count : int
                The maximum number of words desired in the summary.

            Returns:
            --------
            str
                The summarized text.

            Examples:
            ---------
            >>> from sinlingua.summarizer.tf_idf import TFIDFTextSummarizer
            >>> text_summarizer = TFIDFTextSummarizer()
            >>> sample_text = "පාර්ලිමේන්තුවේ කාර්ය මණ්ඩලයේ සිටින ඇතැම් කාන්තාවන් එම කාර්ය මණ්ඩලයේම සිටින පිරිමින් අතින් අපහරණයට ලක්වූ බව අප පසුගිය දිනයේ කියෙව්වෙමු. මේ පිළිබඳ පරීක්‍ෂා කිරීම සඳහා දැනටමත් සාමාජිකයන් තුන්දෙනකුගෙන් සමන්විත කමිටුවක් පත්කොට තිබේ. සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. මෙය ඉතා භයානක තත්ත්වයකි. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය. හඳුනාගත් වහාම ඔවුන්ගේ වැඩ තහනම් කළ යුතුය. කථානායකතුමා මේ කාර්යය සම්බන්ධයෙන් දැඩිව සිටින බව අපට විශ්වාසය. පාර්ලිමේන්තු මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි මෙය රට කරවන ප්‍රමුඛ ආයතනය වූ පාර්ලිමේන්තුවට එල්ල කරන ලද මඩ පහරකි. මේ පිළිබඳ තනිව නැගී සිට හඬ නැගීම ගැන රෝහිණී කවිරත්නට ස්තුතිවන්ත වෙමු. මේ අතර පසුගිය දිනවල පාර්ලිමේන්තුවේ මන්ත්‍රීවරියන්ට වාචිකව කරන ලද ලිංගික අඩන්තේට්ටම ගැනද දැනගන්නට ලැබිණ. යුද බිමේ තිබෙන ස්ත්‍රී අපහරණය නමැති නීච ආයුධය පාර්ලිමේන්තුව තුළට ගෙන ඒමට ඉඩදිය යුතු නැත."
            >>>
            >>> summary = text_summarizer.summarize_by_word_count(sample_text, word_count=500)
            >>> print(summary)
            පාර්ලිමේන්තුවේ කාර්ය මණ්ඩලයේ සිටින ඇතැම් කාන්තාවන් එම කාර්ය මණ්ඩලයේම සිටින පිරිමින් අතින් අපහරණයට ලක්වූ බව අප පසුගිය දිනයේ කියෙව්වෙමු. මේ පිළිබඳ පරීක්‍ෂා කිරීම සඳහා දැනටමත් සාමාජිකයන් තුන්දෙනකුගෙන් සමන්විත කමිටුවක් පත්කොට තිබේ. සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. මෙය ඉතා භයානක තත්ත්වයකි. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය. හඳුනාගත් වහාම ඔවුන්ගේ වැඩ තහනම් කළ යුතුය. කථානායකතුමා මේ කාර්යය සම්බන්ධයෙන් දැඩිව සිටින බව අපට විශ්වාසය. පාර්ලිමේන්තු මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි මෙය රට කරවන ප්‍රමුඛ ආයතනය වූ පාර්ලිමේන්තුවට එල්ල කරන ලද මඩ පහරකි. මේ පිළිබඳ තනිව නැගී සිට හඬ නැගීම ගැන රෝහිණී කවිරත්නට ස්තුතිවන්ත වෙමු. මේ අතර පසුගිය දිනවල පාර්ලිමේන්තුවේ මන්ත්‍රීවරියන්ට වාචිකව කරන ලද ලිංගික අඩන්තේට්ටම ගැනද දැනගන්නට ලැබිණ. යුද බිමේ තිබෙන ස්ත්‍රී අපහරණය නමැති නීච ආයුධය පාර්ලිමේන්තුව තුළට ගෙන ඒමට ඉඩදිය යුතු නැත.

            Notes:
            ------
            - Ensure that the text_corpus is preprocessed for best summarization results.
            - The returned summary will have sentences ordered as they appear in the original text.
            """
        cleaned_sentences, sentences = self.__preprocess_sentences(text)
        _, sentence_vectors = self.__create_tfidf_model(cleaned_sentences)
        sentence_scores = np.array(sentence_vectors.sum(axis=1)).ravel()
        sorted_sentences = [cleaned_sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1]]
        N = 0
        total_words = 0
        for sent in sorted_sentences:
            total_words += len(sent.split())
            if total_words <= word_count:
                N += 1
            else:
                break
        top_n_sentences = [cleaned_sentences[ind] for ind in np.argsort(sentence_scores, axis=0)[::-1][:N]]
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
        >>> from sinlingua.summarizer.tf_idf import TFIDFTextSummarizer
        >>> text_summarizer = TFIDFTextSummarizer()
        >>> sample_text = "පාර්ලිමේන්තුවේ කාර්ය මණ්ඩලයේ සිටින ඇතැම් කාන්තාවන් එම කාර්ය මණ්ඩලයේම සිටින පිරිමින් අතින් අපහරණයට ලක්වූ බව අප පසුගිය දිනයේ කියෙව්වෙමු. මේ පිළිබඳ පරීක්‍ෂා කිරීම සඳහා දැනටමත් සාමාජිකයන් තුන්දෙනකුගෙන් සමන්විත කමිටුවක් පත්කොට තිබේ. සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. මෙය ඉතා භයානක තත්ත්වයකි. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය. හඳුනාගත් වහාම ඔවුන්ගේ වැඩ තහනම් කළ යුතුය. කථානායකතුමා මේ කාර්යය සම්බන්ධයෙන් දැඩිව සිටින බව අපට විශ්වාසය. පාර්ලිමේන්තු මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි මෙය රට කරවන ප්‍රමුඛ ආයතනය වූ පාර්ලිමේන්තුවට එල්ල කරන ලද මඩ පහරකි. මේ පිළිබඳ තනිව නැගී සිට හඬ නැගීම ගැන රෝහිණී කවිරත්නට ස්තුතිවන්ත වෙමු. මේ අතර පසුගිය දිනවල පාර්ලිමේන්තුවේ මන්ත්‍රීවරියන්ට වාචිකව කරන ලද ලිංගික අඩන්තේට්ටම ගැනද දැනගන්නට ලැබිණ. යුද බිමේ තිබෙන ස්ත්‍රී අපහරණය නමැති නීච ආයුධය පාර්ලිමේන්තුව තුළට ගෙන ඒමට ඉඩදිය යුතු නැත."
        >>>
        >>> summarized_text = text_summarizer.summarize_by_percent(sample_text, percent=20)
        >>> translated_text = text_summarizer.translate_to_english(summarized_text)
        >>> print(translated_text)
        සමගි ජනබලවේගයේ මන්ත්‍රී රෝහිණී කවිරත්න කියන පරිදි පෙර කී කාන්තාවන් අපහරණ කළ කාම දුර්ජනයන් විසින් එම චෝදනාව ප්‍රතික්‍ෂේප කරන ලිපියක් අපහරණයට පත්වූ කාන්තාවන් ලවා අත්සන් කර ගැනීමට උත්සාහ කර තිබේ. පාර්ලිමේන්තුවේ සිටින පිරිමි සේවක මණ්ඩලය විශාල නොවන බැවින් පෙර කී ලිංගික පිස්සන් සමූහය කවරේදැයි හඳුනාගැනීමට ඉතා පහසුය.

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


