import streamlit as st
from gtts import gTTS
from IPython.display import display, Audio

# Function to convert French text to French speech using gTTS
def text_to_speech_french(text, output_file):
    """
    Convert French text to speech using Google Text-to-Speech (gTTS) and play the audio.

    Parameters:
        text (str): The French text to convert to speech.
        output_file (str): The filename to save the output audio file (e.g., 'output.mp3').
    """
    tts = gTTS(text=text, lang='fr', slow=False)
    tts.save(output_file)
    audio = Audio(output_file)
    display(audio)

def main():
    st.title("Text Translator and Text-to-Speech")

    # Input text from the user
    text = st.text_area("Enter text to translate:", value="")

    if st.button("Text-to-Speech (French)"):
        if text.strip():
            output_filename = "french_audio.mp3"
            text_to_speech_french(text, output_filename)
            st.audio(output_filename)
        else:
            st.warning("Please enter some text for Text-to-Speech.")
            
if __name__ == "__main__":
    main()
