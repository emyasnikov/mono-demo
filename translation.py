import config
import deepl

auth_key = config.get('DEEPL_AUTH_KEY')
target_lang = config.get('DEEPL_TARGET_LANG')

def translate(input):
    if config.get('DEEPL') == 'true':
        translator = deepl.Translator(auth_key)

        return translator.translate_text(input, target_lang=target_lang)

    return input
