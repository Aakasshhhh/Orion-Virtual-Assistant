import speech_recognition as sr # Line 1

def take_command():
    """
    Captures audio with noise calibration and 
    improves recognition accuracy for the name 'ORION'.
    """
    
    # Line 2: Initialize the Recognizer
    r = sr.Recognizer() 
    
    # Line 3: Access the Microphone
    with sr.Microphone() as source: 
        # --- ACCURACY BOOST 1: Noise Calibration ---
        print("\n[SYSTEM]: Calibrating for background noise... Please wait.")
        # Line 4: Listens to the room for 1 sec and adjusts the sensitivity
        r.adjust_for_ambient_noise(source, duration=1) 
        
        print("[SYSTEM]: Listening...") # Line 5
        
        # Line 6: Parameters for better response
        r.pause_threshold = 1.0  # Wait for 1 sec gap before stopping
        r.operation_timeout = 5  # Timeout if no speech is detected
        
        # Line 7: Record the audio
        audio = r.listen(source) 

    try:
        print("[SYSTEM]: Recognizing...") # Line 8
        
        # Line 9: Recognize using Google API (Indian English accent)
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}") # Line 10
        
        # --- ACCURACY BOOST 2: Fuzzy Name Mapping ---
        # Convert to lowercase for uniform checking
        query = query.lower() 
        
        # List of words Google often misidentifies for 'ORION'
        wrong_names = ['aryan', 'orient', 'ocean', 'ryan', 'onion', 'audio', 'aaryan', 'alien', 'Narayan']
        
        # If any of these are found, we replace them with 'orion'
        for name in wrong_names:
            if name in query:
                query = query.replace(name, 'orion')
        
    except sr.UnknownValueError:
        # Line 11: Runs if audio is too faint or noisy to understand
        print("[SYSTEM]: Error: Speech was unintelligible.")
        return "none"
        
    except sr.RequestError:
        # Line 12: Runs if there is no internet connection
        print("[SYSTEM]: Error: Google Service is down or Internet is missing.")
        return "none"
        
    except Exception as e:
        # Line 13: General catch-all for other errors
        return "none"
        
    # Line 14: Return the finalized, corrected string
    return query

# --- TESTING BLOCK ---
if __name__ == "__main__":
    # Test it 1 time to check accuracy
    for i in range(1):
        command = take_command()
        print(f"Orion heard: {command}")