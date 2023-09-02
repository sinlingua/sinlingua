from fuzzywuzzy import fuzz
from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.src.grammar_rule_resources import question_verbs


class FourthPerson(GrammarRules):
    def common_function(self, sentence):
        global conjugated_sentence
        grammar_obj = GrammarRules()
        conjugated_verb = ''
        returned_string_verb = grammar_obj.find_similar_words(question_verbs, sentence)
        # call the function find verb of sentence
        verb_checked = returned_string_verb[0]
        actual_word = returned_string_verb[1]
        ratio = returned_string_verb[2]
        if returned_string_verb[0]:
            # Extract the verb stem
            verb_stem = verb_checked[:-1]
            # Remove the last word (verb) from the sentence
            words = sentence.split()
            words.remove(actual_word)
            # Check if the sentence starts with "තී", "තෝ", "ඔබ", "නුඹ"
            if sentence.split()[0] in ["තී", "තෝ", "ඔබ", "නුඹ"]:
                if verb_stem[-1] in ["ා"]:
                    verb_stem = verb_stem[:-1]
                conjugated_verb = verb_stem + "ෙහි"
            # Check if the sentence starts with "අපි"
            elif sentence.split()[0] in ["තෙපිි", "තොපි"]:
                if verb_stem[-1] in ["ා"]:
                    verb_stem = verb_stem[:-1]
                conjugated_verb = verb_stem + "ෙහු"
            # Append the conjugated verb to the sentence
            words.append(conjugated_verb)
            # Reconstruct the sentence
            conjugated_sentence = " ".join(words)

        if conjugated_verb == '':
            return "Try Again..Incomplete sentence. No enough data to process", ratio

        else:
            return conjugated_sentence, ratio
