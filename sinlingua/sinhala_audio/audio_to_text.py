import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def conversion(path: str):
    """
    Convert a speech audio file to text.

    This function reads an audio file and performs speech recognition using the Google Speech Recognition API.
    The recognized text is printed to the console.

    Parameters:
    -----------
    path : str
        The path to the audio file. Default is 'r../../resources/datasets/IT20167264/test_audio/pn_sin_01_00003.wav'.

    Returns:
    --------
    None

    Raises:
    -------
    None

    Notes:
    ------
    - Make sure you have the required dependencies installed, such as the SpeechRecognition library.
    - The language parameter can be modified to specify a different language for speech recognition.
    - The audio file should be in a compatible format supported by the SpeechRecognition library.
    """
    lang = 'si-LK'

    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)
        try:
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language=lang)
            return text
        except Exception as e:
            print(f'Sorry.. run again...{str(e)}')


def conversion_by_input():
    """
    Perform speech-to-text grammar_rule on an audio file.

    This function uses the SpeechRecognition library to recognize the speech in an audio file and convert it into text.

    Parameters:
    -----------
    None

    Returns:
    --------
    None

    Raises:
    -------
    UnknownValueError:
        If the speech recognition system could not understand the audio.
    RequestError:
        If there was an error during the speech recognition request.


    Notes:
    ------
    - Make sure you have the required dependencies installed, such as the SpeechRecognition library and the required speech recognition API keys.
    - The audio file should be in a compatible format supported by the SpeechRecognition library.
    - The language parameter can be modified to specify a different language for speech recognition.

    """
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Read the audio file path from user input
    audio_file = input("Enter the path to the audio file: ")

    # Perform speech recognition
    with sr.AudioFile(audio_file) as source:
        print('Fetching File')
        audio_text = recognizer.listen(source)
        try:
            print('Converting audio transcripts into text ...')
            text = recognizer.recognize_google(audio_text, language='si-LK')
            return text
        except sr.UnknownValueError:
            print('Speech recognition could not understand audio')
        except sr.RequestError as e:
            print(f'Error occurred during speech recognition: {e}')
