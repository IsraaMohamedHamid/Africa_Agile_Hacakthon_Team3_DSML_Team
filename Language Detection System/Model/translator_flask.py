# app.py
from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

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

# Function to get the full language name based on the language code
def get_language_name(lang_code):
    lang_dict = {
        'af': 'Afrikaans',
        'ar': 'Arabic',
        'ny': 'Nyanja',
        'en': 'English',
        'fr': 'French',
        'ha': 'Hausa',
        'ig': 'Igbo',
        'mg': 'Malagasy',
        'st': 'Sesotho',
        'sn': 'Shona',
        'so': 'Somali',
        'sw': 'Swahili',
        'xh': 'Xhosa',
        'yo': 'Yoruba',
        'zu': 'Zulu',
    }
    return lang_dict.get(lang_code, '')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    user_text = data['text']
    target_lang_code = data['target_lang']

    if user_text.strip():
        translated_text = translate_text(user_text, target_lang_code)
        response = {'translated_text': translated_text}
    else:
        response = {'error': 'Please enter some text to translate.'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
