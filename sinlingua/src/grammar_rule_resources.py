grammar_rule_llm_config = {
  "api_key":"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",
  "org_key":"org-FAg23PQBtCvq57kZHYd0HYlW",
  "model": "gpt-3.5-turbo",
  "temperature": 0,
  "max_tokens": 2000,
  "Top_P": 1,
  "Frequency_penalty": 0,
  "Presence_penalty": 0,
  "max_characters": 4000,
  "TC_Only": "NO",
  "Prompts": [
    {
      "role": "user",
      "content": "I need you to identify the given Sinhala word singular or plural. Make sure to give the output in the following JSON structure.\nJSON structure:\n{\n     \"<word>\": \"<singular/plural>\"\n}\n\nWord: '{{word}}'"
    },
    {
      "role": "user",
      "content": ""
    }
  ]
}

nouns_subject_plural = [
    "ගුරුවරු",
    "ළමයි",
    "ශිෂ්‍යයෝ",
    "මව්වරු",
    "පියවරු",
    "දෙමව්පියෝ",
    "සත්තු",
    "දොස්තරවරු",
    "ගායකයො",
    "ප්‍රේක්ශකයො",
    "නලුවො",
    "සන්ගීතකාරයො",
    "මනුස්ස්‍යො",
    "මනුශ්‍යයෝ",
    "වදුරෝ",
    "ගොවියෝ",
    "රජවරු",
    "නායකයෝ",
    "මිනිස්සු",
    "සාමාජිකයෝ",
    "සමූහයෝ",
    "දරුවෝ",
    "පාත්තයෝ",
    "කුරුල්ලෝ",
    "බල්ලෝ",
    "පටව්",
    "බබාලා",
    "මීයෝ",
    "පූසෝ",
    "මාළු",
    "දෙවියෝ",
    "වැද්දෝ",
    "කපුටෝ",
    "දිම්යෝ",
    "කඩියෝ",
    "අලි",
    "යාලුවො",
    "යාළුවො",
    "කැල",
    "සමූහය",
    "රැල",
    "රන්චුව",
    "පෙල",
    "රචකයො",
    "ලේඛකයෝ",
    "ඇදුරෝ",
    "කථිකාචාර්යවරු",
    "නිලියෝ",
    "නිළයෝ",
    "ඉන්ජිනේරුවරු",
    "කොන්දොස්තරවරු",
    "නිලධාරියෝ",
    "සර්පයෝ",
    "කතුවරු",
    "මනාලියෝ",
    "මනාලයෝ",
    "කුමාරියෝ",
    "කුමාරයෝ",
    "කැරපොත්තො",
    "වැඩිහිටියෝ",
    "කොල්ලො",
    "කෙල්ලො",
    "යක්කු",
    "හිමිවරු",
    "ශ්‍රමිකයෝ",
    "කම්කරුවෝ",
    "ශ්‍රමනයෝ",
    "ශ්‍රමණයෝ",
    "ගණිකාවො",
    "කාන්තාවෝ",
    "පිරිමි",
    "අය",
    "නාටිකාන්ගනාවෝ",
    "අන්ගනාවො",
    "කසකරුවෝ",
    "ගිනිබෝලකරුවෝ",
    "විදේශිකයෝ",
    "පෙම්වත්තු",
    "පෙම්වතියෝ",
    "ප්‍රේමවන්තයෝ",
    "ධීවරයෝ",
    "පෙදරේරුවෝ",
    "කාර්මිකයෝ",
    "තරඟකරුවෝ",
    "ජයග්‍රාහකයො",
    "පරාජිකයෝ",
    "ක්‍රීඩකයෝ",
    "දායකයෝ",
    "පාලකයෝ",
    "දේශපාලකයෝ",
    "සිරකරුවෝ",
    "නිලදාරීවරු",
    "වරු",
    "පිරිස",
    "පාහරයෝ",
    "ආක්‍රමණිකයෝ",
    "ද්‍රෝහියෝ",
    "සේවකයෝ",
    "සහෝදරියෝ",
    "සහෝදරයෝ",
    "අම්මලා",
    "තාත්තලා",
    "කුරුමිනියෝ"
]

nouns_subject_singular = [
    "ගුරුවරයා",
    "ළමයා",
    "ශිෂ්‍යයා",
    "මව්වරයා",
    "පියා",
    "සතා",
    "දොස්තරවරයා",
    "ගායකයා",
    "ප්‍රේක්ශකයා",
    "නලුවා",
    "සන්ගීතකාරයා",
    "මනුස්ස්‍යා",
    "මනුශ්‍යයා",
    "වදුරා",
    "ගොවියා",
    "රජා",
    "නායකයා",
    "මිනිසා",
    "සාමාජිකයා",
    "දරුවා",
    "පාත්තයා",
    "කුරුල්ලා",
    "බල්ලා",
    "පටවා",
    "බබා",
    "මීයා",
    "පූසා",
    "මාළුවා",
    "දෙවියා",
    "වැද්දා",
    "කපුටා",
    "දිම්යා",
    "කඩියා",
    "අලියා",
    "යාලුවා",
    "යහලුවා",
    "යහළුවා",
    "යාළුවා",
    "රචකයා",
    "ලේඛකයා",
    "ඇදුරුතුමා",
    "වෙදදුරුතුමා",
    "කථිකාචාර්යවරයා",
    "නිලිය",
    "නිළය",
    "ඉන්ජිනේරු",
    "මහතා",
    "කොන්දොස්තරවරයා",
    "නිලධාරියා",
    "සර්පයා",
    "කතුවරයා",
    "මනාලිය",
    "මනාලයා",
    "කුමාරිය",
    "කුමාරයා",
    "කැරපොත්තා",
    "වැඩිහිටා",
    "කොල්ලා",
    "කෙල්ල",
    "යකා",
    "හිමිනමක්",
    "ශ්‍රමිකයා",
    "කම්කරුවා",
    "ශ්‍රමනයා",
    "ශ්‍රමණයා",
    "ගණිකාව",
    "කාන්තාව",
    "පිරිමියා",
    "අය",
    "නාටිකාන්ගනාව",
    "අන්ගනාව",
    "කසකරුවා",
    "ගිනිබෝලකරුවා",
    "විදේශිකයා",
    "පෙම්වතා",
    "පෙම්වතිය",
    "ප්‍රේමවන්තයා",
    "ධීවරයා",
    "පෙදරේරුවා",
    "කාර්මිකයා",
    "තරඟකරුවා",
    "ජයග්‍රාහකයා",
    "පරාජිකයා",
    "ක්‍රීඩකයා",
    "දායකයා",
    "පාලකයා",
    "දේශපාලකයා",
    "සිරකරුවා",
    "නිලදාරීවරයා",
    "වරයා",
    "පාහරයා",
    "ආක්‍රමණිකයා",
    "ද්‍රෝහියා",
    "සේවකයා",
    "සහෝදරියා",
    "සහෝදරයා",
    "අම්මා",
    "තාත්තා",
    "අමර",
    "කුරුමිනියා"
]

past_verbs = [
    "කෑවා",
    "නෑවා",
    "හෑවා",
    "ආවා",
    "ගියා",
    "බිව්වා",
    "කැඩුවා",
    "නැටුවා",
    "සේදුවා",
    "හේදුවා",
    "මැරුවා",
    "පැගුවා",
    "හැකිලුවා",
    "දිව්වා",
    "කැපුවා",
    "කලා",
    "කෙරුවා",
    "කිව්වා",
    "කැවුනා",
    "දැනුනා",
    "බැලුවා",
    "නිවුනා",
    "පියෑඹුවා",
    "පිලිස්සුවා",
    "හිනැහුනා",
    "ගත්තා",
    "උනා",
    "වුනා",
    "පෑව්වා",
    "හැපුවා",
    "පීරුවා",
    "නැරඹුවා",
    "ගැයුවා",
    "වැයුවා",
    "දැමුවා",
    "කෙරුවා",
    "වැන්දා",
    "නැමුනා",
    "පිම්බා",
    "නැග්ගා",
    "බැස්සා",
    "නැග්ගුවා",
    "ගෑවා",
    "රිංගුවා",
    "පීනුවා",
    "හෑරුවා",
    "හිතුවා",
    "සිතුවා",
    "ඇන්දා",
    "පැලදුවා",
    "හැදුවා",
    "මැසුවා",
    "ගෙතුවා",
    "ඉව්වා",
    "ඇරියා",
    "වැහුවා",
    "පැන්නා",
    "මැහුවා",
    "නෙළුවා",
    "නෙලුවා",
    "සැපයුවා",
    "සිටියා"
]

question_verbs = [
    "කරාද",
    "ලිව්වද",
    "මැරුවද",
    "නැවද",
    "පෙව්වද",
    "සේදුවද",
    "හේදුවද",
    "ගියාද",
    "ආවද",
    "බිව්වද",
    "වැඩියද",
    "පැමිනියද",
    "විසඳුවද",
    "පැන්නද",
    "කැඩුවද",
    "කලාද",
    "දුන්නද",
    "දිව්වද",
    "බැලුවද",
    "නැටුවද",
    "ඇහුවද",
    "ඉන්නවද",
    "හදනවද",
    "උවයනවද",
    "යනවද",
    "පෙරලුනාද",
    "වැටුනද",
    "ගත්තද",
    "නෑවද"
]

verbs = [
    "පාගනවා",
    "දුවනවා",
    "නටනවා",
    "බොනවා",
    "සිතනවා",
    "ගන්නවා",
    "බලනවා",
    "හදනවා",
    "අතුගානවා",
    "අමදිනවා",
    "පුරනවා",
    "හිඳිනවා",
    "හෝදනවා",
    "සෝදනවා",
    "නිදාගන්නවා",
    "අමතනවා",
    "කියනවා",
    "පිරිමදිනවා",
    "සලනවා",
    "එවනවා",
    "කරනවා",
    "වාඩිවෙනවා",
    "අරිනවා",
    "ඉරෙනවා",
    "ඉරනවා",
    "ඉතිරෙනවා",
    "පිපිරෙනවා",
    "සිනාසෙනවා",
    "හිනාවෙනවා",
    "වෙනවා",
    "තැවෙනවා",
    "රවනවා",
    "ඔරවනවා",
    "පාවෙනවා",
    "ලියනවා",
    "ගහනවා",
    "කොටනවා",
    "කපනවා",
    "මහනවා",
    "පදිනවා",
    "වනවා",
    "එලවනවා",
    "ලියලනවා",
    "නානවා",
    "නාවනවා",
    "කැවෙනවා",
    "කනවා",
    "ඇවිදිනවා",
    "පීනනවා",
    "ඇදෙනවා",
    "ඇසෙනවා",
    "ඇහෙනවා",
    "පේනවා",
    "ඇරෙනවා",
    "වසනවා",
    "වහනවා",
    "වැහෙනවා",
    "නරඹනවා",
    "පළදනවා",
    "නිදියනවා",
    "සැතපෙනවා",
    "සතපවනවා",
    "නමදිනවා",
    "වඳිනවා",
    "වදිනවා",
    "ඇනෙනවා",
    "වැටෙනවා",
    "මරනවා",
    "යනවා",
    "බුරනවා",
    "සපයනවා",
    "යවනවා",
    "දානවා",
    "දෙනවා",
    "බලවනවා",
    "කසනවා",
    "හොයනවා",
    "සොයනවා",
    "තියෙනවා",
    "නමනවා",
    "උයනවා",
    "ඉන්නවා",
    "උගන්වනවා",
    "මහනවා",
    "ආදරෙයි",
    "නගිනවා",
    "පනිනවා",
    "කඩනවා"
]

verbs_2f = [
    "පාගාවි",
    "දුවාවි",
    "නටාවි",
    "බොයි",
    "සිතාවි",
    "ගනීවි",
    "බලාවි",
    "හදාවි",
    "අතුගාවි",
    "අමදීවි",
    "පුරාවි",
    "හිදීවි",
    "හෝදාවි",
    "සෝදාවි",
    "නිදාගනීවි",
    "අමතාවි",
    "කියාවි",
    "පිරිමදීවි",
    "සලාවි",
    "ඒවි",
    "කරාවි",
    "වාඩිවේවි",
    "අරීවි",
    "ඉරේවි",
    "ඉතිරේවි",
    "පිපිරේවි",
    "සිනාසේවි",
    "තැවේවි",
    "රවාවි",
    "ඔරවාවි",
    "පාවේවි",
    "ලියාවි",
    "නාවි",
    "කාවි",
    "ඇදිදීවි",
    "වේවි",
    "පීනාවි",
    "ඇදේවි",
    "ඇරේවි",
    "වසාවි",
    "නරඹාවි",
    "පළදාවි",
    "නිදියාවි",
    "සැතපේවි",
    "නමදීවි",
    "පතන්නාම්",
    "නාවන්නම්",
    "නාන්නම්",
    "බලවාවි",
    "බලන්නම්",
    "කරවන්නම්",
    "ඇරෙන්නම්",
    "කන්නම්",
    "ගයන්නම්",
    "පතන්නම්",
    "වඳින්නම්",
    "නටන්නම්",
    "කරන්නම්",
    "ඉඳීම්",
    "හිඳීවි",
    "ඉඳීවි",
    "බලන්නම්",
    "නාවන්නම්",
    "නාන්නම්",
    "සිතන්නම්",
    "පාගන්නම්",
    "ලියන්නම්",
    "නිදියන්නම්",
    "ඇහිඳින්නම්",
    "ගලපන්නම්",
    "අඳින්නම්",
    "අදින්නම්",
    "නමන්නම්",
    "බොන්නම්",
    "උයන්නම්",
    "හදන්නම්",
]