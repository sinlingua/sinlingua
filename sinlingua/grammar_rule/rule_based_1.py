from fuzzywuzzy import fuzz
from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.src.grammar_rule_resources import verbs

class FirstPerson(GrammarRules):
    def common_function(self, sentence):
        global conjugated_sentence
        grammar_obj = GrammarRules()
        conjugated_verb = ''
        returned_string_verb = grammar_obj.find_similar_words(verbs, sentence)
        # call the function find verb of sentence
        verb_checked = returned_string_verb[0]
        actual_word = returned_string_verb[1]
        ratio = returned_string_verb[2]
        if returned_string_verb[0]:
            if verb_checked == 'ගන්නවා':
                verb_checked = 'ගනිනවා'
            elif verb_checked == 'පෙන්නනනවා':
                verb_checked = 'පෙන්වනවා'
            elif verb_checked == 'ගන්නනනවා':
                verb_checked = 'ගන්වනවා'
            elif verb_checked == 'නිදාගන්නවා':
                verb_checked = 'නිදාගනිනවා'
            elif verb_checked == 'ඉන්නවා':
                verb_checked = 'ඉන්නෙනවා'
            elif verb_checked == 'ආදරෙයි':
                verb_checked = 'ආදරය කරනවා'
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
                conjugated_verb = verb_stem + "මි"
                # Add the first word as "මම" to the sentence
                words[0] = "මම"
            # Check if the sentence starts with "අපි"
            elif sentence.split()[0] in ["අපි", "අප"] or (
                    len(sentence.split()) > 1 and sentence.split()[1] in ["අපි", "අප"]):
                if len(words) > 1 and words[1] in ["අපි", "අප"]:
                    words.pop(0)
                # Add the first word as "අපි" to the sentence
                words[0] = "අපි"
                conjugated_verb = verb_stem + "මු"
            # Append the conjugated verb to the sentence
            words.append(conjugated_verb)
            # Reconstruct the sentence
            conjugated_sentence = " ".join(words)

        if conjugated_verb == '':
            return "Try Again..Incomplete sentence. No enough data to process", ratio

        else:
            return conjugated_sentence, ratio
