import config
import deepl
import transformers

auth_key = config.get('DEEPL_AUTH_KEY')
target_lang = config.get('DEEPL_TARGET_LANG')

def translate(input, max_length=512):
    if config.get('DEEPL') == 'true':
        translator = deepl.Translator(auth_key, server_url=config.get('DEEPL_SERVER_URL'))

        return translator.translate_text(input, target_lang=target_lang)

    translator = transformers.pipeline(config.get('TRANSLATION_MODEL'), max_length=max_length)

    return translator(input)[0]['translation_text']
