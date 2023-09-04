from sinlingua.grammar_rule.grammar_rules import GrammarRules, translate_sinhala_to_english
from googletrans import Translator
from sinlingua.src.grammar_rule_resources import past_verbs, nouns_subject_plural


class PluralSubjectPast(GrammarRules):
    def common_function(self, sentence):
        grammar_obj = GrammarRules()
        global conjugated_sentence
        prefixes = ["මා", "අපි", "මම", "ම", "අප", "ඔහු", "ඇය", "ඈ", "ඔවුන්", "ඔවුහු"]
        conjugated_verb = ''

        # split the sentence
        wordlist = sentence.split()

        # call the function find verb of sentence
        returned_string_verb_past = grammar_obj.find_similar_words(past_verbs, wordlist[-1])

        verb_checked_past = returned_string_verb_past[0]

        actual_word_past = returned_string_verb_past[1]

        # call the function find subject of sentence
        returned_string_subject_past = grammar_obj.find_similar_words(nouns_subject_plural, wordlist[0])

        subject_checked_past = returned_string_subject_past[0]

        actual_subject_past = returned_string_subject_past[1]

        ratio = returned_string_subject_past[2]

        if returned_string_verb_past[0]:
            # Extract the verb stem
            verb_stem = verb_checked_past[:-1]
            if returned_string_subject_past[0]:
                sentence = sentence.replace(actual_subject_past, subject_checked_past)
            # Split the sentence
            words = sentence.split()

            if returned_string_subject_past[0]:
                # Adding "ති" for the stem
                conjugated_verb = verb_stem + "ෝය"

                # Remove the last word (verb) from the sentence
                words.remove(actual_word_past)
                words.append(conjugated_verb)

                # Reconstruct the sentence
                conjugated_sentence = " ".join(words)

            elif any(sentence.startswith(prefix) or sentence.split()[1] == prefix for prefix in prefixes):
                conjugated_verb = ''

            else:
                words.remove(actual_word_past)

                conjugated_verb = verb_stem + "මින් ඇත"

                words.append(conjugated_verb)

                # Reconstruct the sentence
                conjugated_sentence = " ".join(words)

                # print("Sorry.........This may be wrong. No enough data to process_plural")
                """"# Translate Sinhala sentence to English
                english_translation = translate_sinhala_to_english(' '.join(words))
                print(english_translation)"""

        if conjugated_verb == '':
            return "Try Again..Incomplete sentence. No enough data to process", ratio

        else:
            return conjugated_sentence, ratio
