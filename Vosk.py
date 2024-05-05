import sys
from vosk import Model, KaldiRecognizer
import wave
import json

def transcribe_audio(file_path):
    # Load Vosk model
    model = Model("path_to_vosk_model_folder")  # e.g., "./models/vosk-model-small-en-us-0.15"
    
    # Open the audio file
    wf = wave.open(file_path, "rb")
    
    # Create a recognizer with the model
    rec = KaldiRecognizer(model, wf.getframerate())
    
    # Process the audio
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    
    # Get final result
    results.append(json.loads(rec.FinalResult()))

    # Return only the text parts
    return ' '.join([res['text'] for res in results if 'text' in res])

if __name__ == "__main__":
    result = transcribe_audio(sys.argv[1])
    print(result)
