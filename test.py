import googletrans
from pprint import pprint


# Initial
translator = googletrans.Translator()


# Basic Translate
results = translator.translate('我覺得今天天氣不好。')
print(results)
print(results.text)