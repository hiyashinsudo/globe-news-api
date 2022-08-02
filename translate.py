from googletrans import Translator


def get_translation(original_text: str):
    return Translator().translate(original_text, src="en", dest="ja").text
