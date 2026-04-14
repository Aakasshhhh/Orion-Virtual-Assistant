import pyttsx3

def speak(text):
    # We initialize the engine INSIDE the function to refresh the connection 
    # every time ORION speaks. This prevents the "skip" bug in loops.
    engine = pyttsx3.init('sapi5')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    
    print(f"[ORION]: {text}")
    
    # Queue the text
    engine.say(text)
    
    # This MUST be here to wait for the audio to finish 
    # before letting the listener start again.
    engine.runAndWait()
    
    # Force stop to clear the buffer
    engine.stop()