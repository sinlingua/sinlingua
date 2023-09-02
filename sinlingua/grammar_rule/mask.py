import requests
from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.grammar_rule.LLM_config import LLMConfig
from sinlingua.src.grammar_rule_resources import verbs


class PredictNoun(GrammarRules):
    def common_function(self, sentence):
        # llm = LLMConfig()

        grammar_obj = GrammarRules()
        global conjugated_sentence
        conjugated_verb = ''
        returned_string_verb = grammar_obj.find_similar_words(verbs, sentence)
        verb_checked = returned_string_verb[0]
        actual_word = returned_string_verb[1]
        ratio = returned_string_verb[2]
        if returned_string_verb[0]:
            # Extract the verb stem
            verb_stem = verb_checked[:-1]
            # Remove the last word (verb) from the sentence
            words = sentence.split()
            words.remove(actual_word)

            # Get gpt output for singular/plural
            # llm_dict = llm.llm_check(word=words[0], level=0)
            # if llm_dict[words[0]]:
            #     sing_plu = llm_dict[words[0]]
            # else:
            #     sing_plu = "singular"

            # print(words[0])
            # print(sing_plu)
