alphabet = {
  "vowels": {
      "a": "අ",
      "A": "අ",
      "aa": "ආ",
      "Aa": "ආ",
      "ae": "ඇ",
      "Ae": "ඇ",
      "aee": "ඈ",
      "Aee": "ඈ",
      "i": "ඉ",
      "I": "ඉ",
      "ii": "ඊ",
      "Ii": "ඊ",
      "u": "උ",
      "U": "උ",
      "uu": "ඌ",
      "Uu": "ඌ",
      "ERU": "ඍ",
      "ERU'": "ඎ",
      "IRU": "ඏ",
      "IRU'": "ඐ",
      "e": "එ",
      "E": "එ",
      "ee": "ඒ",
      "Ee": "ඒ",
      "ai": "ඓ",
      "Ai": "ඓ",
      "o": "ඔ",
      "O": "ඔ",
      "oo": "ඕ",
      "Oo": "ඕ",
      "au": "ඖ",
      "Au": "ඖ",
      "x": "(අං)",
      "X": "(අඃ)"
  },
  "consonants": {
      "k": "ක",
      "c": "ක",
      "K": "ක",
      "kh": "ඛ",
      "Kh": "ඛ",
      "g": "ග",
      "G": "ඝ",
      "gh": "ඝ",
      "Gh": "ඝ",
      "ng": "ඞ",
      "nng": "ඟ",
      "zg": "ඟ",
      "ch": "ච",
      "Ch": "ඡ",
      "j": "ජ",
      "J": "ඣ",
      "jh": "ඣ",
      "ngj": "ඤ",
      "zk": "ඤ",
      "ny": "ඤ",
      "Ngj": "ඥ",
      "jny": "ඥ",
      "nyj": "ඦ",
      "zj": "ඦ",
      "t": "ට",
      "T": "ඨ",
      "d": "ඩ",
      "D": "ඪ",
      "N": "ණ",
      "zd": "ඬ",
      "nd": "ඬ",
      "th": "ත",
      "Th": "ථ",
      "dh": "ද",
      "Dh": "ධ",
      "n": "න",
      "ndh": "ඳ",
      "p": "ප",
      "P": "ඵ",
      "ph": "ඵ",
      "r": "ර",
      "l": "ල",
      "L": "ළ",
      "s": "ස",
      "sh": "ශ",
      "Sh": "ෂ",
      "h": "හ",
      "w": "ව",
      "v": "ව",
      "f": "ෆ",
      "b": "බ",
      "B": "භ",
      "bh": "භ",
      "m": "ම",
      "mb": "ඹ",
      "y": "ය"
  },
  "dependent_vowels": {
      "aa": "ා",
      "ae": "ැ",
      "aae": "ෑ",
      "i": "ි",
      "ii": "ී",
      "u": "ු",
      "uu": "ූ",
      "ERU": "ෘ",
      "e": "ෙ",
      "ee": "ේ",
      "ai": "ෛ",
      "o": "ො",
      "oo": "ෝ",
      "au": "ෞ",
      "x": "ං"
  }
}

config_data = {
  "api_key": "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",
  "org_key": "org-FAg23PQBtCvq57kZHYd0HYlW",
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
      "content": "I can provide you a sentence with some spelling errors. Your goal is to accurately identify the misspelled Sinhala words. \n\nThe output should be presented in JSON format, structured as follows:\n\n{\n    \"word_list\": [\n          \"<first_incorrect_word>\",\n          \"<second_incorrect_word>\",\n          ...............,\n          \"<last_incorrect_word>\"\n     ]\n}\nMake sure to use only the words which is not exist in the Sinhala language as \"<first_incorrect_word>\", \"<second_incorrect_word>\",  ..............., \"<last_incorrect_word>\".\n\nSentence: '{{masked-sentence}}'"
    },
    {
      "role": "user",
      "content": "I can provide you with a version of the word with some spelling errors. Your goal is to accurately identify the most suitable Sinhala word that matches the given misspelled version for the specified <mask>. Please note that the word you suggest should indeed exist in the Sinhala language (Real Word). Decide the category of the misspelled word as well. Word categories are subject, predicate, object, complement, and modifier. Get the help of this to decide the word as well.\n\nThe output should be presented in JSON format, structured as follows:\n\n{\n    \"<misspelled_word>\": \"<correct_word>\",\n     \"category\": \"<category_from_given_list>\"\n}\n\nSentence with the <mask>: '{{masked-sentence}}'\nMisspelled word: '{{misspelled-word}}'"
    }
  ]
}

