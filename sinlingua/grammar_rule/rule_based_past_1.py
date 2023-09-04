from fuzzywuzzy import fuzz
from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.src.grammar_rule_resources import past_verbs


class PastFirstPerson(GrammarRules):
    def common_function(self, sentence):
        global conjugated_sentence
        grammar_obj = GrammarRules()
        conjugated_verb = ''

        # call the function find verb of sentence
        returned_string_verb_past = grammar_obj.find_similar_words(past_verbs, sentence)

        verb_checked_past = returned_string_verb_past[0]

        actual_word_past = returned_string_verb_past[1]

        ratio_past = returned_string_verb_past[2]

        if returned_string_verb_past[0]:
            verb_stem_past = verb_checked_past[:-1]

            # Split the sentence and Remove the last word (verb) from the sentence
            words = sentence.split()
            words.remove(actual_word_past)

            # Check if the sentence starts with "මම" or "මා"
            if sentence.split()[0] in ["මම", "මා"] or (
                    len(sentence.split()) > 1 and sentence.split()[1] in ["මම", "මා"]):
                if len(words) > 1 and words[1] in ["මම", "මා"]:
                    words.pop(0)
                conjugated_verb = verb_stem_past + "ෙමි"

                # Add the first word as "මම" to the sentence
                words[0] = "මම"

            # Check if the sentence starts with "අපි"
            elif sentence.split()[0] in ["අපි", "අප"] or (
                    len(sentence.split()) > 1 and sentence.split()[1] in ["අපි", "අප"]):
                if len(words) > 1 and words[1] in ["අපි", "අප"]:
                    words.pop(0)

                # Add the first word as "අපි" to the sentence
                words[0] = "අපි"
                conjugated_verb = verb_stem_past + "ෙමු"

            # Append the conjugated verb to the sentence
            words.append(conjugated_verb)

            # Reconstruct the sentence
            conjugated_sentence = " ".join(words)

        if conjugated_verb == '':
            return "Try Again..Incomplete sentence. No enough data to process", ratio_past

        else:
            return conjugated_sentence, ratio_past
