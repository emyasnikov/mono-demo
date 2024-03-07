import deepl

auth_key = ''
target_lang = 'DE'
translator = deepl.Translator(auth_key)

def translate(input):
    return translator.translate_text(input, target_lang=target_lang)
