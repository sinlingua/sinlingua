from sinlingua.grammar_rule.grammar_rules import GrammarRules, translate_sinhala_to_english
from googletrans import Translator
from sinlingua.src.grammar_rule_resources import verbs, nouns_subject_plural


class PluralSubject(GrammarRules):
    def common_function(self, sentence):
        grammar_obj = GrammarRules()
        global conjugated_sentence
        prefixes = ["මා", "අපි", "මම", "ම", "අප", "ඔහු", "ඇය", "ඈ", "ඔවුන්", "ඔවුහු"]
        conjugated_verb = ''

        # call the function find verb of sentence
        returned_string_verb = grammar_obj.find_similar_words(verbs, sentence)

        verb_checked = returned_string_verb[0]

        actual_word = returned_string_verb[1]

        # call the function find subject of sentence
        returned_string_subject = grammar_obj.find_similar_words(nouns_subject_plural, sentence)

        subject_checked = returned_string_subject[0]

        actual_subject = returned_string_subject[1]

        ratio = returned_string_subject[2]
        if returned_string_verb[0]:
            # Extract the verb stem
            verb_stem = verb_checked[:-3]

            if returned_string_subject[0]:
                sentence = sentence.replace(actual_subject, subject_checked)

            words = sentence.split()

            if returned_string_subject[0]:
                if verb_stem[-1] in ["්"]:
                    verb_stem = verb_stem[:-1]
                    verb_stem = verb_stem + "ි"

                # Adding "ති" for the stem
                conjugated_verb = verb_stem + "ති"

                # Split the sentence and Remove the last word (verb) from the sentence
                words.remove(actual_word)
                words.append(conjugated_verb)

                # Reconstruct the sentence
                conjugated_sentence = " ".join(words)

            elif any(sentence.startswith(prefix) or sentence.split()[1] == prefix for prefix in prefixes):
                conjugated_verb = ''

            else:
                words.remove(actual_word)

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
