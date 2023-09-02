# -*- coding: utf-8 -*-
from transformers import DistilBertTokenizer, DistilBertModel, LongformerTokenizer, LongformerModel
import torch
from sinling import SinhalaTokenizer
from googletrans import Translator
import numpy as np
import string
from sklearn.metrics.pairwise import cosine_similarity

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
    "එහෙත්"]  # Define the Sinhala stopword list

class FLongformerTextSummarizer:
    def __init__(self):
        self.tokenizer = SinhalaTokenizer()
        self.stopwords = stopwords
        self.punctuation = punctuation
        self.distilbert_tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-multilingual-cased')
        self.distilbert_model = DistilBertModel.from_pretrained('distilbert-base-multilingual-cased')
        self.longformer_tokenizer = LongformerTokenizer.from_pretrained('allenai/longformer-base-4096')
        self.longformer_model = LongformerModel.from_pretrained('allenai/longformer-base-4096')
        self.translator = Translator()

    def __preprocess_sentences(self, text_corpus):
        sentences = self.tokenizer.split_sentences(text_corpus)
        sentences = [sent.strip() for sent in sentences]
        cleaned = [sent for sent in sentences if sent not in self.stopwords and sent not in self.punctuation]
        return cleaned, sentences

    def __create_distilbert_embeddings(self, cleaned_sentences):
        sentence_embeddings = []
        for sent in cleaned_sentences:
            inputs = self.distilbert_tokenizer.encode_plus(sent, return_tensors="pt", max_length=512, truncation=True, padding='max_length')
            with torch.no_grad():
                output = self.distilbert_model(**inputs)
            sentence_embeddings.append(output.last_hidden_state.mean(dim=1).squeeze().numpy())
        return np.array(sentence_embeddings)

    def __create_longformer_embeddings(self, cleaned_sentences):
        sentence_embeddings = []
        for sent in cleaned_sentences:
            inputs = self.longformer_tokenizer.encode_plus(sent, return_tensors="pt", max_length=4096, truncation=True, padding='max_length')
            with torch.no_grad():
                output = self.longformer_model(**inputs)
            sentence_embeddings.append(output.last_hidden_state.mean(dim=1).squeeze().numpy())
        return np.array(sentence_embeddings)

    def __append_fullstop(self, text):
        if text and text[-1] not in punctuation:
            return text + '.'
        return text

    def __get_summary(self, embeddings, original_sentences, word_limit):
        avg_embedding = np.mean(embeddings, axis=0).reshape(1, -1)
        cosine_similarities = cosine_similarity(embeddings, avg_embedding).squeeze()
        current_count = 0
        selected_sentences = []
        sorted_sentences = [original_sentences[i] for i in cosine_similarities.argsort()[::-1]]
        for sentence in sorted_sentences:
            tokens = self.tokenizer.tokenize(sentence)
            if current_count + len(tokens) <= word_limit:
                current_count += len(tokens)
                selected_sentences.append(sentence)
            if current_count >= word_limit:
                break
        sentence_organizer = {k: v for v, k in enumerate(original_sentences)}
        mapped_sentences = [(cleaned, sentence_organizer[cleaned]) for cleaned in selected_sentences]
        mapped_sentences = sorted(mapped_sentences, key=lambda x: x[1])
        ordered_sentences = [element[0] for element in mapped_sentences]
        summary = " ".join([self.__append_fullstop(sentence) for sentence in ordered_sentences])
        return summary

    def refined_summarize_by_word_count(self, text, distilbert_word_limit=300, longformer_word_limit=100):
        """
        Generate a refined summary of the given text using DistilBert followed by Longformer embeddings.

        The method first leverages DistilBert embeddings to create an initial summary and then uses Longformer embeddings to refine the summary further. This two-step approach aims to retain the core semantic meaning of the original text while providing a concise summary.

        Parameters:
        -----------
        text : str
            The text to be summarized.
        distilbert_word_limit : int, optional (default = 300)
            The word limit for the summary generated using DistilBert embeddings.
        longformer_word_limit : int, optional (default = 100)
            The word limit for the final refined summary generated using Longformer embeddings.

        Returns:
        --------
        str
            The refined summarized text.

        Notes:
        ------
        - The method prioritizes retaining the semantic meaning of the original text.
        - Ensure that the text is preprocessed for optimal summarization results.
        - The returned summary will have sentences ordered as they appear in the original text.
        """
        cleaned, original = self.__preprocess_sentences(text)
        distilbert_embeddings = self.__create_distilbert_embeddings(cleaned)
        initial_summary = self.__get_summary(distilbert_embeddings, original, distilbert_word_limit)
        cleaned_refined, _ = self.__preprocess_sentences(initial_summary)
        longformer_embeddings = self.__create_longformer_embeddings(cleaned_refined)
        final_summary = self.__get_summary(longformer_embeddings, cleaned_refined, longformer_word_limit)
        return final_summary

    def translate_to_english(self, text):
        """
        Translate the provided text from Sinhala to English.

        Utilizes the Translator class to perform the translation. It might fail for various reasons such as exceeding translation API limits, network issues, etc.

        Parameters:
        -----------
        text : str
            The text in Sinhala to be translated to English.

        Returns:
        --------
        str
            The translated text in English.

        Notes:
        ------
        - Ensure that you have an active internet connection for the translation process.
        - Translation quality might vary based on the complexity of the text.
        - Handle potential exceptions that might arise from the translation API.
        """
        try:
            return self.translator.translate(text, src='si', dest='en').text
        except Exception as e:
            print(f"Error during translation: {str(e)}")
            return ""

