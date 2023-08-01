from gtts import gTTS

def text_to_speech(text, language, output_file):
    """
    Convert text to speech for a given language and save it as an audio file.

    Parameters:
        text (str): The text to convert to speech.
        language (str): The language code ('en' for English, 'yo' for Yoruba, 'ig' for Igbo, 'ha' for Hausa).
        output_file (str): The filename to save the output audio file.
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

if __name__ == "__main__":
    text_to_convert = "Bawo ni?"  # Text to convert to speech
    language_code = "yo"  # 'en' for English, 'yo' for Yoruba, 'ig' for Igbo, 'ha' for Hausa
    output_filename = "yoruba_audio.mp3"
    text_to_speech(text_to_convert, language_code, output_filename)
