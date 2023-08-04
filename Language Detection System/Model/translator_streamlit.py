import streamlit as st
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

def main():
    st.title("Text Translator")
    st.write("Enter text to translate and select the target language from the dropdown.")

    # Input text from the user
    text = st.text_area("Enter text to translate:", value="") #TODO: ADD SENDER USER MESSAGE 

    # Target language selection
    target_lang_code = st.selectbox(
        "Select the target language:",
        options=['af', 'ar', 'ny', 'en', 'fr', 'ha', 'ig', 'mg', 'st', 'sn', 'so', 'su', 'sw', 'xh', 'yo', 'zu'],
        format_func=get_language_name,  # Display full language name
        index=0
    )#TODO: SHOULD BE DETECTED DEPENDING ON THE RECIPIENTS SYSTEM LANGUAGE

    if st.button("Translate"):
        if text.strip():
            translated_text = translate_text(text, target_lang_code)
            st.write("Translated Text:", translated_text)
        else:
            st.warning("Please enter some text to translate.")


if __name__ == "__main__":
    main()
