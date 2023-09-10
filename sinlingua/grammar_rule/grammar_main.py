from sinlingua.grammar_rule.grammar_rules import GrammarRules
from sinlingua.grammar_rule.rule_based_1 import FirstPerson
from sinlingua.grammar_rule.rule_based_2 import SecondPersonSingular
from sinlingua.grammar_rule.rule_based_3 import SecondPersonPlural
from sinlingua.grammar_rule.rule_based_4 import FourthPerson
from sinlingua.grammar_rule.rule_based_future_1 import FirstPersonFuture
from sinlingua.grammar_rule.rule_based_plural import PluralSubject
from sinlingua.grammar_rule.rule_based_plural_past import PluralSubjectPast
from sinlingua.grammar_rule.rule_based_singular import SingularSubject
from sinlingua.grammar_rule.rule_based_past_1 import PastFirstPerson
from sinlingua.grammar_rule.rule_based_past_2 import PastSecondPersonSingular
from sinlingua.grammar_rule.rule_based_past_3 import PastSecondPersonPlural
from sinlingua.grammar_rule.mask import PredictNoun
# Imported all grammar rules together in grammar main


class GrammarMain:
    def _init_(self):
        pass

    @staticmethod
    def mapper(sentence: str):
        """
        :param sentence:
        :return:

        Examples
        -------
        >>> from sinlingua.grammar_rule.grammar_main import GrammarMain
        >>> obj = GrammarMain()
        >>> text = "අපි පොසොන් පෝයට දන්සලක් සංවිධානය කරවා"
        >>> out = obj.mapper(sentence=text)
        >>> print(out)
        අපි පොසොන් පෝයට දන්සලක් සංවිධානය කරමු
        """
        first_person = FirstPerson()
        output1 = first_person.common_function(sentence)
        # print(output1)
        # call the grammar rules for first person

        second_person_singular = SecondPersonSingular()
        output2 = second_person_singular.common_function(sentence)
        # print(output2)
        # call the grammar rules for second person singular

        second_person_plural = SecondPersonPlural()
        output3 = second_person_plural.common_function(sentence)
        # print(output3)
        # call the grammar rules for second person plural

        first_person_future = FirstPersonFuture()
        output4 = first_person_future.common_function(sentence)
        # print(output4)
        # call the grammar rules for first person future

        plural_subject = PluralSubject()
        output5 = plural_subject.common_function(sentence)
        # print(output5)
        # call the grammar rules for plural subjects

        singular_subject = SingularSubject()
        output6 = singular_subject.common_function(sentence)
        # print(output6)
        # call the grammar rules for Singular subjects

        past_first_person = PastFirstPerson()
        output7 = past_first_person.common_function(sentence)
        # print(output7)
        # call the grammar rules for first person past

        past_second_person_singular = PastSecondPersonSingular()
        output8 = past_second_person_singular.common_function(sentence)
        # print(output8)
        # call the grammar rules for second person past singular

        past_second_person_plural = PastSecondPersonPlural()
        output9 = past_second_person_plural.common_function(sentence)
        # print(output9)
        # call the grammar rules for second person past plural

        noun_predict = PredictNoun()
        output10 = noun_predict.common_function(sentence)
        # print(output10)
        # call the grammar rules for predict noun

        plural_subject_past = PluralSubjectPast()
        output11 = plural_subject_past.common_function(sentence)
        # print(output11)
        # call the grammar rules for past plural

        fourth_person = FourthPerson()
        output12 = fourth_person.common_function(sentence)
        # print(output12)
        # call the grammar rules for fourth person

        grammar_rule = GrammarRules()
        # create parent class object
        validated1 = grammar_rule.output(output1[0])
        validated2 = grammar_rule.output(output2[0])
        validated3 = grammar_rule.output(output3[0])
        validated4 = grammar_rule.output(output4[0])
        validated5 = grammar_rule.output(output5[0])
        validated6 = grammar_rule.output(output6[0])
        validated7 = grammar_rule.output(output7[0])
        validated8 = grammar_rule.output(output8[0])
        validated9 = grammar_rule.output(output9[0])
        validated11 = grammar_rule.output(output11[0])
        validated12 = grammar_rule.output(output12[0])
        # validated10 = grammar_rule.output(output10)
        # call function for every grammar rule at once to get correct output

        # Check all outputs are None
        if validated1 is None and validated2 is None and validated3 is None and validated4 is None and validated5 is None and validated6 is None and validated7 is None and validated8 is None and validated9 is None and validated11 is None and validated12 is None:
            return sentence
        # Check First Person Rules and their Similarity Ratios
        if validated1 is not None and validated7 is not None:
            if output1[1] < output7[1]:
                return output7[0]
            if output1[1] > output7[1]:
                return output1[0]
            if output1[1] == output7[1]:
                return output7[0]
        elif validated1 is not None:
            return output1[0]
        elif validated4 is not None:
            return output4[0]
        elif validated7 is not None:
            return output7[0]
        # Check Second Person rules and their Similarity Ratios
        elif validated2 is not None and validated8 is not None:
            if output2[1] < output8[1]:
                return output8[0]
            if output2[1] > output8[1]:
                return output2[0]
            if output2[1] == output8[1]:
                return output2[0]
        elif validated8 is not None:
            return output8[0]
        elif validated2 is not None:
            return output2[0]
        # Check Third Person Rules and their Similarity Ratios
        elif validated3 is not None and validated9 is not None:
            if output3[1] < output9[1]:
                return output9[0]
            if output3[1] > output9[1]:
                return output3[0]
            if output3[1] == output9[1]:
                return output3[0]
        elif validated9 is not None:
            return output9[0]
        elif validated3 is not None:
            return output3[0]
        # Check Fourth Person Rules and their Similarity Ratios
        elif validated12 is not None:
            return output12[0]
        # Check Plural & Singular Rules and their Similarity Ratios
        elif validated5 is not None and validated6 is not None and validated11 is not None:
            if output5[1] < output6[1]:
                if output6[1] < output11[1]:
                    return output11[0]
                return output6[0]
            if output5[1] > output6[1]:
                if output5[1] < output11[1]:
                    return output11[0]
                return output5[0]
            if output5[1] == output6[1]:
                return output6[0]
        elif validated5 is not None and validated6 is not None:
            if output5[1] < output6[1]:
                return output6[0]
            if output5[1] > output6[1]:
                return output5[0]
            if output5[1] == output6[1]:
                return output6[0]
        elif validated5 is not None:
            return output5[0]
        elif validated6 is not None:
            return output6[0]
        elif validated11 is not None:
            return output11[0]
        # if function returns any correct output is returned


# if _name_ == "__main__":
    # obj = GrammarMain()
    # sent = "සංගමයේ සාමාජිකයින් සමිතිය අවසන් බැවින් විසිය යනව"
    # out = obj.mapper(sentence=sent)
    # print(out)

# මා සතුන්ට දානයක් දෙන්න හිතන් ඉන්නවා
# මා සතුන්ට දානයක් දෙන්න හිතන් ඉන්වා
# අපි පොසොන් පෝයට දන්සලක් සංවිධානය කරනවා
# අපි පොසොන් පෝයට දන්සලක් සංවිධානය කරවා
# අප පොසොන් පෝයට දන්සලක් සංවිධානය කරවා
# ඇය පිටිසර පාසලක උත්සහයෙන් උගන්වනවා
# ඇය පිටිසර පාසලක උත්සහයෙන් උගන්නවා
# ඈ පිටිසර පාසලක උත්සහයෙන් උගන්නවා
# ඔහු ඉතා ආදරයෙන් දෙමාපියන් නමදිනව
# ඔවුන් නොයෙක් ආකාරයේ ඇඳුම් මහනවාලු
# ඔවුන් නොයෙක් ආකාරයේ ඇඳුම් මහනව
# ඔවුහු නොයෙක් ආකාරයේ ඇඳුම් මහනව
# අප හෙට මේ වෙලාවට නිදාගෙන හිඳීවි
# මම මේ ටික හොඳට බලන් කියලා දෙන්නම්
# ගොවියෝ මහන්සි වී රටට සහල් සපයනවා
# සංගමයේ සාමාජිකයින් සමිතිය අවසන් බැවින් විසිය යනව
# ඇය මල් නෙලුවා
# ඔහු මල් නෙලුව
# තී මල් කැඩුවද
# තොපි ආහාර ලෑස්ති කරාද
# ගුරුවරු පිටතට පැමිණ සිටියා
# දරුවා වෙහෙස මහන්සියෙන් ඉගෙන ගන්නවා