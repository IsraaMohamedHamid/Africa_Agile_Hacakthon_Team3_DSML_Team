# translate.py
import sys
from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Function to perform translation
def translate_text(text, target_lang):
    """
    Translates the input text to the specified target language.

    Parameters:
        text (str): The text to be translated.
        target_lang (str): The target language code (e.g., 'yo' for Yoruba, 'ha' for Hausa, 'ig' for Igbo).

    Returns:
        str: The translated text in the target language.
    """
    # Detect the source language of the input text
    source_lang = translator.detect(text).lang

    # Perform translation
    translated_text = translator.translate(text, src=source_lang, dest=target_lang).text

    return translated_text

if __name__ == "__main__":
    # Read input from Node.js backend
    text = sys.argv[1]
    target_lang_code = sys.argv[2]

    # Perform translation
    translated_text = translate_text(text, target_lang_code)

    # Send the translated text back to the Node.js backend
    print(translated_text)
