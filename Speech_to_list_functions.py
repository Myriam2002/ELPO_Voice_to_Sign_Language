# Python files to install
    # !pip install SpeechRecognition
    # !pip install PyAudio
    # !pip install Wave
    # !pip install keyboard
# Helper functions
import pyaudio
import wave
import keyboard
import speech_recognition as sr
# F
def record_sound():

    """Records the voice of the user and outputs a file called "output.wav".

    Returns:
        0 if successful.
    """
    # Define some parameters
    FORMAT = pyaudio.paInt16 # Sample format
    CHANNELS = 1 # Number of channels
    RATE = 16000 # Sample rate
    CHUNK = 1024 # Chunk size
    WAVE_FILE = "output.wav" # Output file name

    # Initialize PyAudio object
    p = pyaudio.PyAudio()

    # Create a stream object
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    frames_per_buffer=CHUNK,
                    input=True)

    # Start recording when 's' is pressed
    print("Press 's' to start recording")
    keyboard.wait('s')
    print("Recording...")

    # Store the frames as a list
    frames = []

    # Stop recording when 'q' is pressed
    while not keyboard.is_pressed('q'):
        # Read data from the stream
        data = stream.read(CHUNK)
        # Append to the frames list
        frames.append(data)

    print("Recording stopped")

    # Close and terminate the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the frames as a .wav file
    wf = wave.open(WAVE_FILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return 0

def speech_to_list(file):
    """Takes the recorded file "output.wav" and converts it to text, then only picks words that are within our 10 words.

    Returns:
        a list of ordered words that are within the list of words said .
    """
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(file) as source:
        
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
        
        except:
            print('Sorry.. run again...')
    
    words = []
    ten_words = ["drink","eat","hello","help","love","morning","okay","please","stop","thank you"]
    list_text = text.split(" ")
    for i in list_text:
        if i in ten_words:
            words.append(i)
    return words
        
def speech(file):
    """ Records the WAV file from the user
    Takes the recorded file "output.wav" and converts it to text, then only picks words that are within our 10 words.

    Returns:
        a list of ordered words that are within the list of words said .
    """
    record_sound()
    output_list = speech_to_list(file)
    return output_list
    