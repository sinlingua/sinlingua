from fuzzywuzzy import fuzz
from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.src.grammar_rule_resources import verbs_2f


class FirstPersonFuture(GrammarRules):
    def common_function(self, sentence):
        global conjugated_sentence
        grammar_obj = GrammarRules()
        conjugated_verb = ''
        returned_string_verb = grammar_obj.find_similar_words(verbs_2f, sentence)
        verb_checked = returned_string_verb[0]
        actual_word = returned_string_verb[1]
        ratio = returned_string_verb[2]
        if returned_string_verb[0]:
            # Extract the verb stem
            verb_stem = verb_checked[:-3]
            # Remove the last word (verb) from the sentence
            words = sentence.split()
            words.remove(actual_word)
            # Check if the sentence starts with "මම" or "මා"
            if sentence.split()[0] in ["මම", "මා"] or (
                    len(sentence.split()) > 1 and sentence.split()[1] in ["මම", "මා"]):
                if len(words) > 1 and words[1] in ["මම", "මා"]:
                    words.pop(0)
                if verb_stem[-2:] == 'න්':
                    verb_stem = verb_stem[:-2]
                conjugated_verb = verb_stem + "න්නෙමි"
                # Add the first word as "මම" to the sentence
                words[0] = "මම"
            # Check if the sentence starts with "අපි"
            elif sentence.split()[0] in ["අපි", "අප"] or (
                    len(sentence.split()) > 1 and sentence.split()[1] in ["අපි", "අප"]):
                if len(words) > 1 and words[1] in ["අපි", "අප"]:
                    words.pop(0)
                if verb_stem[-2:] == 'න්':
                    verb_stem = verb_stem[:-2]
                conjugated_verb = verb_stem + "න්නෙමු"
                # Add the first word as "අපි" to the sentence
                words[0] = "අපි"
            # Append the conjugated verb to the sentence
            words.append(conjugated_verb)
            # Reconstruct the sentence
            conjugated_sentence = " ".join(words)
        if conjugated_verb == '':
            return "Try Again..Incomplete sentence. No enough data to process", ratio

        else:
            return conjugated_sentence, ratio

